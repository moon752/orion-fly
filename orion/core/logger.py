import logging
from logging.handlers import RotatingFileHandler

# Setup logger with rotation and format
logger = logging.getLogger("orion")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler("logs/orion.log", maxBytes=5*1024*1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)

