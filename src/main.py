
import logging
import logging.handlers
from src.settings import Settings


def initialize_logging():

    file_handler = logging.handlers.RotatingFileHandler(
        Settings.GLOBAL_LOGS_DIR/Settings.LoggingParams.GLOBAL_FILE_NAME, backupCount=Settings.LoggingParams.BACKUP_COUNT)
    logging.getLogger().addHandler(file_handler)
    file_handler.doRollover()
    logging.info("Global Logging Started")


def main():
    initialize_logging()
    try:
        # Start System
        pass

    except Exception as e:
        logging.exception(e)
        raise e
