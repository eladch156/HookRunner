from Utils.Singleton import Singleton
from Env.EnvSingleton import Environment
import logging
import os
from pathlib import Path
from Utils.Exceptions import ErrorCodes, GeneralException
from Utils.General import LogUtils

IS_DONE = False
FILE_HANDLER = None
STREAM_HANDLER = None
LOG_FORMATER = None


class Logger():
    def __init__(self, *args):
        global FILE_HANDLER
        global STREAM_HANDLER
        global LOG_FORMATER
        global IS_DONE
        self.__main_logger = logging.getLogger("::".join(args))
        self.__env_singleton = Environment()
        _level = LogUtils.str_to_log_level(self.__env_singleton["log_level"])
        self.__main_logger.setLevel(_level)
        if not IS_DONE:
            _log_file_path = str(LogUtils.get_log_file_by_os())
            FILE_HANDLER = logging.FileHandler(_log_file_path, mode='w')
            FILE_HANDLER.setLevel(_level)
            STREAM_HANDLER = logging.StreamHandler()
            STREAM_HANDLER.setLevel(_level)
            LOG_FORMATER = logging.Formatter("[%(asctime)s]"
                                             "[%(levelname)s]"
                                             "[%(name)s]"
                                             "[%(process)d %(thread)d]"
                                             " %(message)s")
            FILE_HANDLER.setFormatter(LOG_FORMATER)
            STREAM_HANDLER.setFormatter(LOG_FORMATER)
            IS_DONE = True
        self.__main_logger.addHandler(FILE_HANDLER)
        self.__main_logger.addHandler(STREAM_HANDLER)

    def log(self, level, fmt, *args):
        _log_level = LogUtils.str_to_log_level(level)
        switch = {
            logging.DEBUG: self.__main_logger.debug,
            logging.INFO: self.__main_logger.info,
            logging.WARNING: self.__main_logger.warning,
            logging.ERROR: self.__main_logger.error,
        }
        if _log_level not in switch:
            raise GeneralException(ErrorCodes.LOG_LEVEL_NO_LOG_FUNCTION,
                                   "Mismatch between 'level'"
                                   " supplied to log function,"
                                   "and available logging functions.")
        else:
            if len(args) == 0:
                switch[_log_level](fmt)
            else:
                switch[_log_level](fmt.format(*args))
