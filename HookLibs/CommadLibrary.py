from enum import Enum
from Utils.Singleton import Singleton
from ctypes import *

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
        self._mapNameToLibInstance = {}
    def libOpen(self, name, path):
        self._mapNameToLibInstance[name] = WinDLL(str(path))

class ApiCommand():
    def __init__(self, libName, funcName):
        self._funcName = funcName
        self._libName = libName
        self._retType = None
        self._argsTypeList = []
        self._libSingleton = LibsSingleton()
    def setReturnType(self, typ):
        self._retType = typ
    def addArgument(self, arg): # arg = (Name, Type)        
        self._argsTypeList.append(arg)
    def run(self, *args):
        function = getLibCmd(self._libSingleton[self._libName], self._funcName, self._retType, self._argsTypeList)
        return function(args)

class LibSpecReader():
    def __init__(self):
        pass