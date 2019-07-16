import logging


class LogDetail:

    def basic_config(self, debug_message=None, info_message=None):
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(level=logging.INFO, datefmt=date_format, format=log_format)
        logging.debug(str(debug_message))
        logging.info(str(info_message))