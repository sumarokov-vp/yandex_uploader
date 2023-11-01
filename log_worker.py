# Standard Library
import logging
import os
import sys

try:
    # Third Party Stuff
    import servicemanager

    win32 = True
except ImportError:
    win32 = False


FOLDER_NAME = "logs"
LOG_FILENAME = os.path.join(FOLDER_NAME, "service.log")


class LogWorker:
    def __init__(self, level=logging.INFO):
        if not os.path.isdir(FOLDER_NAME):
            os.mkdir(FOLDER_NAME)
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
        formatter = logging.Formatter(
            "%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s",
        )

        handler = logging.FileHandler(LOG_FILENAME, "w", "utf-8")
        handler.setLevel(level)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, text):
        if win32:
            servicemanager.LogInfoMsg(text)
        else:
            self.logger.info(text)

    def info(self, text):
        if win32:
            servicemanager.LogInfoMsg(text)
        else:
            self.logger.info(text)

    def error(self, text):
        if win32:
            servicemanager.LogErrorMsg(text)
        else:
            self.logger.error(text)

    def debug(self, text):
        if win32:
            servicemanager.LogInfoMsg(text)
        else:
            self.logger.debug(text)


# l = LogWorker()
