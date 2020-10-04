import logging
from logging.config import dictConfig
import employee_dict
from utils import LOGGING_CONFIG
import time
dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)

def main():
    for i in range(20):
        for j in range(10):
            logger.info('hello_world')
            time.sleep(0.01)
        time.sleep(0.9)

if __name__ == '__main__':
    main()