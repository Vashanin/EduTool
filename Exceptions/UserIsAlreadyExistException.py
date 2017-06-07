import logging

class UserIsAlreadyExistException(BaseException):
    def __init__(self):
        self.__info = "This user is already exist."
        self.log()

    def getInfo(self):
        return self.__info

    def log(self):
        logging.info("somewho try to create already existed user ")