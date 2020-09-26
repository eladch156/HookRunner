from enum import Enum
from io import StringIO
from HookLibs.CommadLibrary import LibsSingleton
from Utils.Singleton import Singleton
from Utils.Exceptions import ErrorCodes,GeneralException
from App.Logger import Logger
from contextlib import redirect_stdout
import logging

class StepType(Enum):
    NONE=0
    ASSERT=1
    VAR=2
    EXECUTE=3
    INCLUDE=4

class StepsData(metaclass=Singleton):
    def __init__(self):
        self._storage = {
            "Variables" : {
            
            },
            "LoadedCommands": []
        }
    def __getitem__(self, key):
        return self._storage[key[0]][key[1]]
    def __setitem__(self, key, value):
        if key[0]=="Variables":
            self._storage[key[0]][key[1]] = value
        elif key[0]=="LoadedCommands": 
            self._storage[key[0]].append(value)
        else:
            pass
    def getFirstCommand(self, name):
        for pair in self._storage["LoadedCommands"]:
            if pair[1] == name:
                return pair
        return None
       

class StepBase():
    def __init__(self):
        self._vars = StepsData()
    def run(self):
        raise NotImplementedError
    def what(self):
        raise NotImplementedError

class StepInclude(StepBase):
    def __init__(self, *args):
        StepBase.__init__(self)
        self._args = args
        self._libSingleton = LibsSingleton()
    def run(self):
        if len(self._args) != 2:
            raise GeneralException(ErrorCodes.HOOK_INC_NOT_VALID,"Hook include must contain only two strings seperated by '.'.")
        if self._libSingleton.loadCommand(self._args[0],self._args[1]):
            self._vars[("LoadedCommands",)] = (self._args[0],self._args[1])
            return True
        else:
            return False
    def what(self):
        return StepType.INCLUDE

class StepRunCommand(StepBase):
    def __init__(self, *args, **kwargs):
        StepBase.__init__(self)
        self._args = args 
        self._cmdName = kwargs["name"] if "name" in kwargs else None
        self._outpipe = kwargs["pipe"] if "pipe" in kwargs else StringIO()
        self._errPipe = StringIO()
        self._libSingleton = LibsSingleton()
        self._logger = Logger("Step","RunCommand")
    def run(self):
        with redirect_stdout(self._outpipe):
            self._libSingleton[self._vars.getFirstCommand(self._cmdName)].run(*self._args)
        self._logger.log(logging.INFO,"Command {} Result: Out='{}',Error='{}'.",self._cmdName,self._outpipe.getvalue(),self._errPipe.getvalue())
        return True
    def what(self):
        return StepType.EXECUTE

class StepDeclVar(StepBase):
    def __init__(self,name,value):
        StepBase.__init__(self)
        self._name = name
        self._value = value
        self._logger = Logger("Step","DeclareVarible")
    def run(self):
        self._logger.log(logging.INFO,"Store ({},{})".format(self._name,self._value))
        self._vars[("Variables",self._name)] =  self._value
    def what(self):
        return StepType.VAR

