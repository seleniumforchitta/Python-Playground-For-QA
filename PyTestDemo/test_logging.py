import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)  # __name__ will capture the testcase file name.
    # if you don't give anything, it will print root

    fileHandler = logging.FileHandler('logFile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    fileHandler.setFormatter(formatter)  # Give format information to logger object
    logger.addHandler(fileHandler)  # fileHandler object - in which file, it has to print
    logger.setLevel(logging.DEBUG)  # set the level of logging

    logger.debug("A debug statement is executed.")
    logger.info("An info statement is executed.")
    logger.warning("A warning statement is executed.")
    logger.error("This is an error message.")
    logger.critical("This is a critical issue.")
