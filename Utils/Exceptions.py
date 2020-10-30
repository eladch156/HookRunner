from enum import Enum


class ErrorCodes(Enum):
    CONFIG_FILE_INCORRECT_STRUCTURE = 1
    CONFIG_FILE_DOESNT_EXIST = 2
    LOG_LEVEL_NO_LOG_FUNCTION = 3
    CANT_EDIT_SPEC_FILE = 4
    INTERNAL_ERROR = 5
    HOOK_INC_NOT_VALID = 6
    COMMUNICATION_DB_ERROR = 7
    NO_LIBRARY_BY_NAME = 8
    NO_COMMAND_BY_NAME = 9
    ANTLR = 10

    def __int__(self):
        return self.value


class GeneralException(Exception):
    def __init__(self, code, message):
        self.__code = code
        self.__message = message
        super().__init__(message)

    def __str__(self):
        return "{}({}) : {}".format(self.__code.name,
                                    self.__code.value,
                                    self.__message)


class AntlrExcption(GeneralException):
    def __init__(self, sub_name, message):
        super(AntlrExcption, self).__init__(ErrorCodes.ANTLR,
                                            "{}::{}".format(sub_name,
                                                            message))
