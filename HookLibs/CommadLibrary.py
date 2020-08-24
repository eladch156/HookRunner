from enum import Enum
from Utils.Singleton import Singleton
from Env.EnvSingleton import Environment
from ctypes import *
import logging
from App.Logger import Logger
from Utils.Exceptions import GeneralException,ErrorCodes
import json
from xml.etree import ElementTree
from json import JSONEncoder

class VarTypes(Enum):
    INT=1
    VOID=2


def strToCType(argType):
    return {
        "char" : c_char,
        "char *": c_char_p,
        "int" : c_int,
        "float" : c_float,
        "double" : c_double,
        "void" : None
    }.get(argType, None)


def getLibCmd(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


class LibsSingleton(metaclass=Singleton):
    def __init__(self):
        self._envSingleton = Environment()
        self._libCfgReader = None
    def __setitem__(self, key, value):
        raise GeneralException(ErrorCodes.CANT_EDIT_SPEC_FILE, "Cannot edit lib spec file.")
    def __getitem__(self, key):
        pass
    def isLibraryExist(self,name):
        return self._libCfgReader.isLibraryExist(name)
    def isCmdExist(self,lib,cmd):
        return self._libCfgReader.isCmdExist(lib,cmd)
    def init(self):
        self._libCfgReader = LibConfigFileReader(self._envSingleton['lib_spec_file'])
        self._libCfgReader.read()
        

def ApiCommandToJson(JSONEncoder):
    def default(self, apiCommand):
        return apiCommand.__str__()


class ApiCommand():
    def __init__(self, libPath, funcName):
        self._funcName = funcName
        self._libPath = libPath
        self._retType = None
        self._argsTypeList = []
    def setReturnType(self, typ):
        self._retType = typ
    def addArgument(self, arg): # arg = (Name, Type)        
        self._argsTypeList.append(arg)
    def run(self, *args):
        function = getLibCmd(WinDLL(str(self._libPath)), self._funcName, self._retType, self._argsTypeList)
        return function(args)
    def __str__(self):
        return "Library={},Function={} {}({})".format(self._libPath,self._retType,self._funcName,",".join(self._argsTypeList))


class LibConfigFileReader():
    def __init__(self, path):
        self._cfgPath = path
        self._cmds = {}
        self._logger = Logger("Library","Loader")
    def read(self):
        root = ElementTree.parse(self._cfgPath).getroot()
        for lib in root:
            specReader = LibSpecReader(lib.attrib['SpecPath'])
            self._cmds[lib.attrib['Name']] = specReader.read()
        self._logger.log(logging.DEBUG, str(self))
    def serialize(self):
        serializedCmds = {}
        for lib in self._cmds:
            serializedCmds[lib] = {}
            for apiCmd in self._cmds[lib]:
                serializedCmds[lib][apiCmd] = str(self._cmds[lib][apiCmd])
        return serializedCmds
    def isLibraryExist(self,name):
        return name in self._cmds
    def isCmdExist(self,lib,cmd):
        return lib in self._cmds and cmd in self._cmds[lib]
    def __str__(self):
        return json.dumps(self.serialize(),indent=4)


class LibSpecReader():
    def __init__(self, path):
        self._specPath = path
    def read(self):
        cmds = {}
        root = ElementTree.parse(self._specPath).getroot()
        libFile = root.attrib['LibFile']
        for function in root:
            funcName = function.attrib['Name']
            cmd = ApiCommand(libFile, funcName)
            cmd.setReturnType(strToCType(function.attrib["Return"]))
            for argument in function:
                 cmd.addArgument((argument.name,strToCType(argument.attrib['Type'])))
            cmds[funcName] = cmd
        return cmds
                
        