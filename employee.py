import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(name)s:[%(levelname)s]:%(message)s")
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('hello 123 ')
