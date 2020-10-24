from enum import Enum
from io import StringIO
from HookLibs.CommadLibrary import LibsSingleton
from Utils.Singleton import Singleton
from Utils.Exceptions import ErrorCodes,GeneralException
from App.Logger import Logger
from contextlib import redirect_stdout
import logging
from Utils.Operators import OperatorUtils

class StepType(Enum):
    NONE=0
    ASSERT=1
    VAR=2
    EXECUTE=3
    INCLUDE=4
    ASSIGNMENT=5

class AssignmentType(Enum):
    FUNCTION=0
    VALUE=1
    VARIBLE=2

class StepsData():
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
            if pair[0] == name:
                return pair[1]
        return None
    def isVaribleExist(self, name):
        for key in self._storage["Variables"]:
            if key == name:
                return True
        return False
    def getVaribleByUuid(self, uuid):
        for key in self._storage["Variables"]:
            if "ID" in self._storage["Variables"][key]:
                if self._storage["Variables"][key]["ID"] == uuid:
                    return key
        return None
    def __str__(self):
        return "Variables = {} || Commands = {}".format(str(self._storage["Variables"]),str(self._storage["LoadedCommands"]))

class StepBase():
    def __init__(self):
        self._vars = None
        self._libSingleton = LibsSingleton()
    def setStepsData(self,data):
        self._vars = data
    def run(self):
        raise NotImplementedError
    def what(self):
        raise NotImplementedError

class StepInclude(StepBase):
    def __init__(self, *args):
        StepBase.__init__(self)
        self._args = args
    def run(self):
        if len(self._args) != 2:
            raise GeneralException(ErrorCodes.HOOK_INC_NOT_VALID,"Hook include must contain only two strings seperated by '.'.")
        LoadedCommand = self._libSingleton.loadCommand(self._args[0],self._args[1])
        if LoadedCommand is not None:
            self._vars[("LoadedCommands",)] = (self._args[1],LoadedCommand)
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
        self._outpipe = kwargs["oPipe"] if "oPipe" in kwargs else StringIO()
        self._errpipe = kwargs["ePipe"] if "ePipe" in kwargs else StringIO()
        self._uuid = kwargs["uuid"] if "uuid" in kwargs else None
        self._logger = Logger("Step","RunCommand")
    def run(self):
        cmd = self._vars.getFirstCommand(self._cmdName)
        ret = cmd(*self._args)
        if self._uuid is not None and ret is not None:
            self._vars[("Variables",self._vars.getVaribleByUuid(self._uuid))]["Value"] = ret
            self._logger.log(logging.INFO, "Command Return : Var = {}, Value = {}", self._vars.getVaribleByUuid(self._uuid), ret)
        self._logger.log(logging.INFO,"Command {} Result: Out='{}', Error='{}'",self._cmdName,self._outpipe.getvalue(),self._errpipe.getvalue())
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
        self._vars[("Variables",self._name)] =  {"Value" : self._value}
    def what(self):
        return StepType.VAR

class StepAssignment(StepBase):
    def __init__(self,name,value,valueType,op):
        StepBase.__init__(self)
        self._name = name
        self._value = value
        self._valueType = valueType
        self._op = op
    def run(self):
        if self._valueType == AssignmentType.FUNCTION:
            if self._vars.isVaribleExist(self._name):
                self._vars[("Variables",self._name)]["ID"] = self._value
                self._vars[("Variables",self._name)]["OP"] = self._op
            else:
                self._vars[("Variables",self._name)] = { "ID": self._value, "OP": self._op }
        elif self._valueType == AssignmentType.VARIBLE:
            if not self._vars.isVaribleExist(self._value):
                #TODO: Error
                pass
            if self._vars.isVaribleExist(self._name):
                self._vars[("Variables",self._name)]["Value"] = OperatorUtils.applyAssignmentOp(self._vars[("Variables",self._name)]["Value"],self._op, self._vars[("Variables",self._value)])
            else:
                if self._op == "=":
                    self._vars[("Variables",self._name)] =  {"Value" : self._vars[("Variables",self._value)] }
                else:
                    #TODO: Error
                    pass
        elif self._valueType == AssignmentType.VALUE:
            if self._vars.isVaribleExist(self._name):
                self._vars[("Variables",self._name)]["Value"] = OperatorUtils.applyAssignmentOp(self._vars[("Variables",self._name)]["Value"],self._op,self._value)
            else:
                if self._op == "=":
                    self._vars[("Variables",self._name)] =  {"Value" : self._value}
                else:
                    #TODO: Error
                    pass
    def what(self):
        return StepType.ASSIGNMENT