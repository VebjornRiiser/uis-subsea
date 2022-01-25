from flask import Flask

app = Flask(__name__)



def recieve_from_main(connection):
    while True:
        app.config["data"] = connection.recv()
    connection = ""
    updater = threading.Thread(target=recieve_from_main, args=(connection,))
    updater.start()



from app import routes

