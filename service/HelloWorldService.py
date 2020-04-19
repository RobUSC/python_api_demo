import logging
logger = logging.getLogger("__main__")


class HelloWorldService:
    pass


def hello_world():
    logger.info('Hello World Logging')
    return 'Hello World!'
