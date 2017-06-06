import logging

class EmptyDatabaseException(Exception):
    def __init__(self, info):
        super(info)
        self.__info = info
        self.log()

    def getInfo(self):
        return self.__info

    def getName(self):
        return "EmptyDatabaseException"

    def log(self):
        logging.info("empty database " + str(self.__info))