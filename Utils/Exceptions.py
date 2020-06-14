from enum import Enum

class ErrorCodes(Enum):
    CONFIG_FILE_INCORRECT_STRUCTURE=1
    CONFIG_FILE_DOESNT_EXIST=2
    LOG_LEVEL_NO_LOG_FUNCTION=3

class GeneralException(Exception):
    def __init__(self,code,message):
        self._code = code
        self._message = message
        super().__init__(message)
    def __str__(self):
        return "{}({}) : {}".format(self._code.name,self._code.value,self._message)
