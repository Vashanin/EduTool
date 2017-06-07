import logging

class SubjectIsAlreadyExistException(BaseException):
    def __init__(self):
        self.__info = "This subject is already exist."
        self.log()

    def getInfo(self):
        return self.__info

    def log(self):
        logging.info("somewho try to create already existed subject")