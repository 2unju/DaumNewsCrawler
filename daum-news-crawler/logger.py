import logging


def make_logger(name=None):
    '''
    from https://greeksharifa.github.io/%ED%8C%8C%EC%9D%B4%EC%8D%AC/2019/12/13/logging/
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s | %(name)s | %(filename)s | %(message)s")

    console = logging.StreamHandler()
    # file_handler = logging.FileHandler(filename="crawler.log")
    #
    console.setLevel(logging.INFO)
    # file_handler.setLevel(logging.DEBUG)
    #
    console.setFormatter(formatter)
    # file_handler.setFormatter(formatter)

    logger.addHandler(console)
    # logger.addHandler(file_handler)

    return logger
