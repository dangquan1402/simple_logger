import logging
import employee

logger = logging.getLogger(__name__)

logging.basicConfig(filemode='a', filename='sample.log', level=logging.DEBUG,
                             format="%(asctime)s:%(name)s:[%(levelname)s]:%(message)s")


def main():
    logger.info('hello')

if __name__ == '__main__':
    main()
