import logging


class Logger:
    def __init__(self):
        logging.basicConfig(filename="log", level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    def info(self, message):
        logging.info(message)

    def error(self, message):
        logging.error(message)
