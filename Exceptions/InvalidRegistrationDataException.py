import logging

class InvalidRegistrationDataException(Exception):
    def __init__(self, info):
        super(info)
        self.__info = info
        self.log()

    def getInfo(self):
        return self.__info

    def getName(self):
        return "InvalidRegistrationDataException"

    def log(self):
        logging.info("invalid registration data " + str(self.__info))