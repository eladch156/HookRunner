from Utils.Singleton import Singleton
from Env.EnvSingleton import Environment
import logging
import os
from pathlib import Path
from Utils.Exceptions import ErrorCodes,GeneralException

def strToLogLevel(strLevel):
    switch = {
        "Debug" : logging.DEBUG,
        "Info" : logging.INFO,
        "Warning" : logging.WARNING,
        "Error" : logging.ERROR
    }
    return logging.INFO if strLevel not in switch else switch[strLevel]

def getLogFileByOs():
    if os.name == "nt":
        dataFolder = Path(os.getenv('APPDATA')) / "HookRunner"
        if not dataFolder.exists():
            dataFolder.mkdir()
        return (dataFolder / "HookRunner.log")
    if os.name == "posix":
        dataFolder = Path("/var/log/HookRunner.log")
        return dataFolder
    raise OSError

class Logger():
    def __init__(self, *args):
        self._mainLogger = logging.getLogger("::".join(args))
        self._envSingleton = Environment()
        level = strToLogLevel(self._envSingleton["log_level"])
        self._mainLogger.setLevel(level)
        self._logFileHandler = logging.FileHandler(str(getLogFileByOs()),mode='w')
        self._logFileHandler.setLevel(level)
        self._logStreamHandler = logging.StreamHandler()
        self._logStreamHandler.setLevel(level)
        self._logFormatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(process)d %(thread)d] %(message)s')
        self._logFileHandler.setFormatter(self._logFormatter)
        self._logStreamHandler.setFormatter(self._logFormatter)
        self._mainLogger.addHandler(self._logFileHandler)
        self._mainLogger.addHandler(self._logStreamHandler)
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

