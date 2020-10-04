import logging
from logging.config import dictConfig
from utils import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)


logger.info('hello world from another side')