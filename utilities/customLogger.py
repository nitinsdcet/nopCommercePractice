import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(level=logging.DEBUG, filename="C:/logs/automation.log",
                            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                            datefmt='%H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger