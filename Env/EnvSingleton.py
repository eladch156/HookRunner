from Utils.Singleton import Singleton
from configparser import ConfigParser
from os.path import exists
from Utils.Exceptions import GeneralException, ErrorCodes


class Environment(metaclass=Singleton):
    def __init__(self):
        self.__hash = {"version": "0.0.1"}
        self.__config_parser = ConfigParser()

    def read(self):
        path = self["configuration_file"]
        if exists(path):
            self.__config_parser.read(path)
        else:
            raise GeneralException(ErrorCodes.CONFIG_FILE_DOESNT_EXIST,
                                   "Configuration file doesn't exist.")
        if "General" not in self.__config_parser:
            raise GeneralException(ErrorCodes.CONFIG_FILE_INCORRECT_STRUCTURE,
                                   "Missing 'General' Section.")
        if "Communication" not in self.__config_parser:
            raise GeneralException(ErrorCodes.CONFIG_FILE_INCORRECT_STRUCTURE,
                                   "Missing 'General' Section.")
        for key in self.__config_parser["General"]:
            self.__hash[key] = self.__config_parser["General"][key]
        for key in self.__config_parser["Communication"]:
            self.__hash[key] = self.__config_parser["Communication"][key]

    def __getitem__(self, key):
        return self.__hash[key] if key in self.__hash else None

    def __setitem__(self, key, value):
        self.__hash[key] = value
