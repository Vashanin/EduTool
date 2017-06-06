import logging

class UserNotFoundException(Exception):
    def __init__(self, info):
        super(info)
        self.__info = info
        self.log()

    def getInfo(self):
        return self.__info

    def getName(self):
        return "UserNotFoundException"

    def log(self):
        logging.info("user is not found " + str(self.__info))