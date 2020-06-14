from Utils.Singleton import Singleton
from configparser import ConfigParser
from os.path import exists
from Utils.Exceptions import GeneralException, ErrorCodes

class Environment(metaclass=Singleton):
    def __init__(self):
        self._hash = { "version" : "0.0.1" }
        self._configParser = ConfigParser()
    def readFromFile(self):
        path = self["configuration_file"]
        if exists(path):
            self._configParser.read(path)
        else:
            raise GeneralException(ErrorCodes.CONFIG_FILE_DOESNT_EXIST,"Configuration file doesn't exist.")
        if "General" not in self._configParser:
            raise GeneralException(ErrorCodes.CONFIG_FILE_INCORRECT_STRUCTURE,"Missing 'General' Section.")
        for key in self._configParser["General"]:
            self._hash[key] = self._configParser["General"][key]
    def __getitem__(self, key):
        return self._hash[key] if key in self._hash else None
    def __setitem__(self, key, value):
        self._hash[key] = value
