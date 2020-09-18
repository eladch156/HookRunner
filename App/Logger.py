from Utils.Singleton import Singleton
from Env.EnvSingleton import Environment
import logging
import os
from pathlib import Path
from Utils.Exceptions import ErrorCodes,GeneralException
from Utils.General import LogUtils

IS_DONE=False
FILE_HANDLER=None
STREAM_HANDLER=None
LOG_FORMATER=None

class Logger():
    def __init__(self, *args):
        global FILE_HANDLER
        global STREAM_HANDLER
        global LOG_FORMATER
        global IS_DONE
        self._mainLogger = logging.getLogger("::".join(args))
        self._envSingleton = Environment()
        level = LogUtils.strToLogLevel(self._envSingleton["log_level"])
        self._mainLogger.setLevel(level)
        if not IS_DONE:
            FILE_HANDLER = logging.FileHandler(str(LogUtils.getLogFileByOs()),mode='w')
            FILE_HANDLER.setLevel(level)
            STREAM_HANDLER = logging.StreamHandler()
            STREAM_HANDLER.setLevel(level)
            LOG_FORMATER = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(process)d %(thread)d] %(message)s')
            FILE_HANDLER.setFormatter(LOG_FORMATER)
            STREAM_HANDLER.setFormatter(LOG_FORMATER)
            IS_DONE = True
        self._mainLogger.addHandler(FILE_HANDLER)
        self._mainLogger.addHandler(STREAM_HANDLER)
    def log(self, level, fmt, *args):
        switch = {
            logging.DEBUG : self._mainLogger.debug,
            logging.INFO : self._mainLogger.info,
            logging.WARNING: self._mainLogger.warning,
            logging.ERROR : self._mainLogger.error,
        }
        if level not in switch:
            raise GeneralException(ErrorCodes.LOG_LEVEL_NO_LOG_FUNCTION,"Mismatch between 'level' supplied to log function, and available logging functions.")
        else:
            if len(args)==0:
                switch[level](fmt)
            else:
                switch[level](fmt.format(*args))

