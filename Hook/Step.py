from enum import Enum
from HookLibs.CommadLibrary import LibsSingleton
from Utils.Singleton import Singleton
from Utils.Exceptions import ErrorCodes,GeneralException

class StepType(Enum):
    NONE=0
    ASSERT=1
    VAR=2
    EXECUTE=3
    INCLUDE=4

class StepExceutor():
    pass

class StepVarMap(metaclass=Singleton):
    def __init__(self):
        self._db = {}
    def __getitem__(self, key):
        return self._db[key]
    def __setitem__(self, key, value):
        self._db[key] = value
    

class StepBase():
    def __init__(self):
        self._vars = StepVarMap()
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
        return self._libSingleton.isCmdExist(self._args[0],self._args[1]) 
    def what(self):
        return StepType.INCLUDE

class StepDeclVar(StepBase):
    def __init__(self,name,value):
        StepBase.__init__(self)
        self._name = name
        self._value = value
    def run(self):
        self._vars[self._name] =  self._value
    def what(self):
        return StepType.VAR

