import logging

class AccessDeniedException(Exception):
    def __init__(self, info):
        super(info)
        self.__info = info
        self.log()

    def getInfo(self):
        return self.__info

    def getName(self):
        return "AccessDeniedException"

    def log(self):
        logging.info("access denied " + str(self.__info))