import threading, socket, time

class Network:

    def __init__(self, is_server=False, bind_addr="127.0.0.1", port=6900, connect_addr="127.0.0.1"):
        self.is_server = is_server
        self.bind_addr = bind_addr
        self.connect_addr = connect_addr
        self.port = port
        
        self.conn = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.new_conn()
        self.heartbeat = threading.thread(target=self.beat)


    def beat(self):
        while True:
            self.send(b"heartbeat")
            time.sleep(0.3)

    def new_conn(self):
        if self.is_server:
            wait_for_conn = threading.thread(target=self.wait_for_conn)
            wait_for_conn.start()
        else:
            self.socket.connect((self.connect_addr, self.port))

    def wait_for_conn(self) -> None:
        while True:
            self.conn, addr = self.socket.accept()
            print(f"New connection from {addr}")


    def send(self, bytes_to_send: bytes) -> None:
        if self.conn is None and self.is_server == False:
            raise("Client tried sending with a non existing connection")
        try:
            self.conn.sendall(bytes_to_send)
        except Exception:
            self.new_conn()

    def receive(self) -> bytes:
        return self.conn.recv()


def send_forever(conn):
    while True:
        

if __name__ == "__main__":
    client_conn = Network()
    server_conn = Network(is_server=True)

    threading.Thread(target = lambda: send_forever(client_conn))
