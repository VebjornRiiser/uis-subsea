
class Logger:
    def __init__(self):
        self.file = open("log.txt", "a")

        self.close()

    def cleanup(self):
        self.file.close()
        
if __name__ == "__main__":
    logger = Logger()
