import logging

class AdminLoginException(RuntimeError):
    def __init__(self):
        self.log()

    def log(self):
        logging.info("Admin is here")