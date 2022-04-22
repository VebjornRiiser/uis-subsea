from datetime import datetime
import logging
import datetime
import os
class Logger:
    def __init__(self):
        self.logfolder = "logs/"
        if not os.path.exists("/logs"): # Need to create logs folder
            os.mkdir(self.logfolder)
        
        formated_date = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")

        # logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
        # logging.basicConfig(filename=f"logs/topside_main {formated_date}.log", format='%(asctime)s %(levelname)s: %(message)s')
        # logging.basicConfig(filename=f"logs/{formated_date}.log")

        log_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

        sensor_filehandler = logging.FileHandler(f"{self.logfolder}{formated_date} sensor.log")
        # error_filehandler = logging.FileHandler(f"{self.logfolder}{formated_date} error.log")

        sensor_filehandler.setFormatter(log_format)
        # error_filehandler.setFormatter(log_format)

        self.sensor_logger = logging.getLogger("sensor_logger")
        # self.error_logger = logging.getLogger("error_logger")

        self.sensor_logger.addHandler(sensor_filehandler)
        self.sensor_logger.setLevel(logging.INFO)

        # self.error_logger.addHandler(error_filehandler)
        # self.error_logger.setLevel(logging.WARNING)

        # self.sensor_logger.info("Start of run")

        
if __name__ == "__main__":
    # formated_date = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    # logger = logging.getLogger()
    # # logger.
    # logger.setLevel(logging.DEBUG)
    # logger.debug("This is a debug message")
    # logger.info("This is a info message")
    # logger.critical("This is a critical message")
    l = Logger()
    