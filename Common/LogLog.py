import logging
from logging.handlers import RotatingFileHandler
from .FilePath import LOG_PATH


class Logger:

    def __init__(self):
        # 创建一个日志收集器
        self.case_logger = logging.getLogger("case")
        # 设置日志收集器登记
        self.case_logger.setLevel("INFO")
        # 创建日志收集器渠道
        self.console_handle = logging.StreamHandler()

        self.file_handle = RotatingFileHandler(filename=LOG_PATH,
                                               mode="a",
                                               maxBytes=1048576,
                                               backupCount=3,
                                               encoding='utf8')
        # 定义日志收集渠道等级
        self.console_handle.setLevel("INFO")
        self.file_handle.setLevel("INFO")

        # 定义日志格式
        fmt = "%(asctime)s - [%(levelname)s] - %(module)s - %(threadName)s - %(name)s - %(lineno)d - [日志信息]:%(message)s"
        self.handel_formatter = logging.Formatter(fmt=fmt)
        self.console_handle.setFormatter(self.handel_formatter)
        self.file_handle.setFormatter(self.handel_formatter)

        # 日志对接渠道
        self.case_logger.addHandler(self.console_handle)
        self.case_logger.addHandler(self.file_handle)

    def get_logger(self):
        return self.case_logger


logger = Logger().get_logger()


if __name__ == '__main__':
    logger.info('测试')