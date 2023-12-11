import inspect
import logging
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # __name__ will capture the testcase file name.
        # if you don't give anything, it will print root

        fileHandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        fileHandler.setFormatter(formatter)  # Give format information to logger object
        logger.addHandler(fileHandler)  # fileHandler object - in which file, it has to print
        logger.setLevel(logging.DEBUG)  # set the level of logging
        return logger
