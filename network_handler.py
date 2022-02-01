import threading
import socket
import sys
import time
import json

global local
local = False
if len(sys.argv) > 1:
    if sys.argv[1] == "True":
        local = True


class Network:

    def __init__(self, is_server=False, bind_addr="127.0.0.1", port=6900, connect_addr="127.0.0.1"):
        self.is_server = is_server
        self.bind_addr = bind_addr
        self.connect_addr = connect_addr
        self.port = port
        self.waiting_for_conn = True
        self.conn = None
        self.timeout = -1

        self.new_conn()
        self.heartbeat = threading.Thread(target=self.beat)
        self.heartbeat.start()

    def beat(self):
        while True:
            self.send(b"heartbeat")
            time.sleep(0.3)

    def new_conn(self):
        self.conn = None
        self.waiting_for_conn = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.is_server:
            print(f"trying to bind with {self.bind_addr, self.port}")
            self.socket.bind((self.bind_addr, self.port))
            self.socket.listen()
            print("starting wait for conn")
            wait_for_conn = threading.Thread(target=self.wait_for_conn)
            wait_for_conn.start()
        else:
            print("Client is trying to connect")
            while True:
                try:
                    self.socket.connect((self.connect_addr, self.port))
                except ConnectionRefusedError:
                    print("Connection refused. Trying again in 500 ms")
                    time.sleep(0.5)
                    continue
                else: # only do this if we do not get an error
                    self.waiting_for_conn = False
                    break
            self.conn = self.socket
            print(f"connection from client has been established. conn: {self.conn}")
            # print(self.socket.gettimeout())
            self.socket.settimeout(0.4)

    def wait_for_conn(self) -> None:
        while True:
            print("Server is waiting on connection")
            self.conn, addr = self.socket.accept()
            self.waiting_for_conn = False

            print(f"New connection from {addr}. conn: {self.conn}, addr")

    def send(self, bytes_to_send: bytes) -> None:
        if self.conn is None and not self.waiting_for_conn:
            raise Exception("Client tried sending with a non existing connection")
        # print(f"waiting for conn: {self.waiting_for_conn}")
        if self.waiting_for_conn:
            print("waiting for conn")
            return
        try:
            if type(bytes_to_send) != bytes:
                print(f"tried sending something that was not bytes: {bytes_to_send} type: {type(bytes_to_send)}")
                exit(1)
            self.conn.sendall(bytes_to_send)
        except socket.error as e: # need to define the actual exceptions we should handle
            print(f"line (56) Tried sending, but got an error \n{e}")
            print(f"conn = {self.conn}, waiting for conn: {self.waiting_for_conn}")
            if not self.waiting_for_conn:
                self.new_conn()

    def receive(self) -> bytes:
        # print(self.conn)
        if self.conn is None:
            if not self.waiting_for_conn:
                self.wait_for_conn()
            return
        try:
            return self.conn.recv(1024)
        except socket.error as e:
            print(f"line 68 Exception: {e}")

    def exit(self):
        self.conn.close()

# Do not get error here if
def send_forever(conn):
    print("sending forever")
    data = {"test": 2, "abc": [1,2,34]}
    data = bytes(json.dumps(data), "utf-8")
    while True:
        conn.send(data)

def recieve_forever():
    pass

if __name__ == "__main__":
    print(sys.platform)
if sys.platform != "win32":
    server_conn = Network(is_server=True, bind_addr="0.0.0.0")
    # server_conn = Network(is_server=True, bind_addr="127.0.0.1")
    # threading.Thread(target=recieve_forever).start()
    while True:
        data = server_conn.receive()
        if not data:
            continue
        print(data)
else:
    client_conn = Network(connect_addr="10.0.0.2")
    send_thread = threading.Thread(target=lambda: send_forever(client_conn))
    send_thread.start()
    send_thread.join()
    while True:
        time.sleep(1)
    