from enum import Enum
from Utils.Singleton import Singleton
from Env.EnvSingleton import Environment
from ctypes import *
import sys
from App.Logger import Logger
from Utils.Exceptions import GeneralException, ErrorCodes
import json
from xml.etree import ElementTree
from json import JSONEncoder


def _str_to_ctype(argType):
    return {
        "char": c_char,
        "char *": c_char_p,
        "int": c_int,
        "float": c_float,
        "double": c_double,
        "long": c_long,
        "long long": c_longlong,
        "void": None
    }.get(argType, None)


def _load_library_file(libPath):
    _type = "CDLL"
    switch = {
        "CDLL": CDLL,
        "WinDLL": WinDLL
    }
    try:
        return switch[_type](libPath)
    except Exception as _:
        return None


def _get_lib_cmd(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


class LibsSingleton(metaclass=Singleton):
    def __init__(self):
        self.__env_singleton = Environment()
        self.__logger = Logger("LibrariesSingleton")
        self.__lib_cfg_reader = None
        self.__cmds = None

    def __setitem__(self, key, value):
        raise GeneralException(ErrorCodes.CANT_EDIT_SPEC_FILE,
                               "Cannot edit lib spec file.")

    def __getitem__(self, key):
        return self.__cmds[key[0]][key[1]]

    def load_command(self, library, command):
        self.__logger.log("Info", "Trying to load {} from {}.".format(command,
                                                                      library))
        if library not in self.__cmds:
            self.__logger.log("Error", "Library {} doesn't exist.".format(
                library))
            return False
        if command not in self.__cmds[library]:
            self.__logger.log("Error", "Command {} doesn't exist.".format(
                command))
            return False
        return self.__cmds[library][command].load()

    def init(self):
        self.__lib_cfg_reader = LibConfigFileReader(
            self.__env_singleton['lib_spec_file'])
        self.__cmds = self.__lib_cfg_reader.read()


def _api_command_to_json(JSONEncoder):
    def default(self, apiCommand):
        return apiCommand.__str__()


class ApiCommand():
    def __init__(self, lib_path, func_name):
        self.__func_name = func_name
        self.__lib_path = lib_path
        self.__ret_type = None
        self.__args_type_list = []
        self.__logger = Logger("Library", "Command")
        self.__function = None

    def set_return_type(self, type_):
        self.__ret_type = type_

    def add_argument(self, arg):
        # arg = (Name, Type)
        self.__args_type_list.append(arg)

    def load(self):
        try:
            return _get_lib_cmd(_load_library_file(self.__lib_path),
                                self.__func_name,
                                self.__ret_type,
                                self.__args_type_list)
        except Exception as ex:
            self.__logger.log("Error", str(ex))
            return None

    def __str__(self):
        _args_text = ",".join(self.__args_type_list)
        return "Library={},Function={} {}({})".format(self.__lib_path,
                                                      self.__ret_type,
                                                      self.__func_name,
                                                      _args_text)


class LibConfigFileReader():
    def __init__(self, path):
        self.__cfg_path = path
        self.__cmds = {}
        self.__logger = Logger("Library", "Loader")

    def read(self):
        root = ElementTree.parse(self.__cfg_path).getroot()
        for lib in root:
            specReader = LibSpecReader(lib.attrib['SpecPath'])
            self.__cmds[lib.attrib['Name']] = specReader.read()
        self.__logger.log("Debug", str(self))
        return self.__cmds

    def serialize(self):
        _serialized_cmds = {}
        for _lib in self.__cmds:
            _serialized_cmds[_lib] = {}
            for _api_cmd in self.__cmds[_lib]:
                _serialized_cmds[_lib][_api_cmd] =\
                    str(self.__cmds[_lib][_api_cmd])
        return _serialized_cmds

    def __str__(self):
        return json.dumps(self.serialize(), indent=4)


class LibSpecReader():
    def __init__(self, path):
        self.__spec_path = path

    def read(self):
        cmds = {}
        root = ElementTree.parse(self.__spec_path).getroot()
        lib_file = root.attrib['LibFile']
        for function in root:
            _func_name = function.attrib['Name']
            _cmd = ApiCommand(lib_file, _func_name)
            _cmd.set_return_type(_str_to_ctype(function.attrib["Return"]))
            for argument in function:
                _cmd.addArgument((argument.name,
                                  _str_to_ctype(argument.attrib['Type'])))
            cmds[_func_name] = _cmd
        return cmds
