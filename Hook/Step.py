from enum import Enum
from io import StringIO
from HookLibs.CommadLibrary import LibsSingleton
from Utils.Singleton import Singleton
from Utils.Exceptions import ErrorCodes, GeneralException
from App.Logger import Logger
from contextlib import redirect_stdout
from Utils.Operators import OperatorUtils


class StepType(Enum):
    NONE = 0
    ASSERT = 1
    VAR = 2
    EXECUTE = 3
    INCLUDE = 4
    ASSIGNMENT = 5


class AssignmentType(Enum):
    FUNCTION = 0
    VALUE = 1
    VARIBLE = 2


class StepsData():
    def __init__(self):
        self.__storage = {
            "Variables": {
            },
            "LoadedCommands": []
        }

    def __getitem__(self, key):
        return self.__storage[key[0]][key[1]]

    def __setitem__(self, key, value):
        if key[0] == "Variables":
            self.__storage[key[0]][key[1]] = value
        elif key[0] == "LoadedCommands":
            self.__storage[key[0]].append(value)
        else:
            pass

    def get_first_command(self, name):
        for pair in self.__storage["LoadedCommands"]:
            if pair[0] == name:
                return pair[1]
        return None

    def is_varible_exist(self, name):
        for key in self.__storage["Variables"]:
            if key == name:
                return True
        return False

    def get_varible_by_uuid(self, uuid):
        for key in self.__storage["Variables"]:
            if "ID" in self.__storage["Variables"][key]:
                if self.__storage["Variables"][key]["ID"] == uuid:
                    return key
        return None

    def __str__(self):
        return "Variables = {} || Commands = {}".format(
                        str(self.__storage["Variables"]),
                        str(self.__storage["LoadedCommands"]))


class StepBase():
    def __init__(self):
        self.vars = None
        self.lib_singleton = LibsSingleton()

    def set_step_data(self, data):
        self.vars = data

    def run(self):
        raise NotImplementedError

    def what(self):
        raise NotImplementedError


class StepInclude(StepBase):
    def __init__(self, *args):
        super().__init__()
        self.__args = args

    def run(self):
        if len(self.__args) != 2:
            raise GeneralException(ErrorCodes.HOOK_INC_NOT_VALID,
                                   "Hook include must "
                                   "contain only two strings "
                                   "seperated by '.'.")
        loaded_command = self.lib_singleton.load_command(self.__args[0],
                                                         self.__args[1])
        if loaded_command is not None:
            self.vars[("LoadedCommands",)] = (self.__args[1], loaded_command)
            return True
        else:
            return False

    def what(self):
        return StepType.INCLUDE


class StepRunCommand(StepBase):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__args = args
        self.__cmd_name = kwargs["name"] if "name" in kwargs else None
        self.__uuid = kwargs["uuid"] if "uuid" in kwargs else None
        self.__logger = Logger("Step", "RunCommand")

    def run(self):
        _cmd = self.vars.get_first_command(self.__cmd_name)
        _ret = _cmd(*self.__args)
        if self.__uuid is not None and _ret is not None:
            self.vars[(
                "Variables",
                self.vars.get_varible_by_uuid(self.__uuid))]["Value"] = _ret
            self.__logger.log("Info",
                              "Command Return : Var = {},"
                              "Value = {}",
                              self.vars.get_varible_by_uuid(self.__uuid),
                              _ret)
        return True

    def what(self):
        return StepType.EXECUTE


class StepDeclVar(StepBase):
    def __init__(self, name, value, uuid=None):
        super().__init__()
        self.__name = name
        self.__value = value
        self.__logger = Logger("Step", "DeclareVarible")
        self.__uuid = uuid

    def run(self):
        if self.__uuid:
            if self.vars.is_varible_exist(self.__name):
                self.vars[("Variables", self.__name)]["ID"] = self.__uuid
                self.vars[("Variables", self.__name)]["OP"] = "="
            else:
                self.vars[("Variables", self.__name)] = {"ID": self.__uuid,
                                                         "OP": "="}
        else:
            self.__logger.log("Info", "Store ({},'{}')".format(self.__name,
                                                               self.__value))
            self.vars[("Variables", self.__name)] = {"Value": self.__value}
        return True

    def what(self):
        return StepType.VAR


class StepAssignment(StepBase):
    def __init__(self, name, value, value_type, op):
        super().__init__()
        self.__name = name
        self.__value = value
        self.__value_type = value_type
        self.__op = op

    def run(self):
        if self.__value_type == AssignmentType.FUNCTION:
            if self.vars.is_varible_exist(self.__name):
                self.vars[("Variables", self.__name)]["ID"] = self.__value
                self.vars[("Variables", self.__name)]["OP"] = self.__op
            else:
                self.vars[("Variables", self.__name)] = {"ID": self.__value,
                                                         "OP": self.__op}
        elif self.__value_type == AssignmentType.VARIBLE:
            if not self.vars.is_varible_exist(self.__value):
                # TODO: Error
                return False
            if self.vars.is_varible_exist(self.__name):
                self.vars[("Variables", self.__name)]["Value"] =\
                    OperatorUtils.apply_assignment_op(
                    self.vars[("Variables", self.__name)]["Value"],
                    self.__op,
                    self.vars[("Variables", self.__value)]["Value"])
            else:
                if self.__op == "=":
                    self.vars[("Variables", self.__name)] =\
                        {"Value": self.vars[("Variables", self.__value)]["Value"]}
                else:
                    # TODO: Error
                    return False
        elif self.__value_type == AssignmentType.VALUE:
            if self.vars.is_varible_exist(self.__name):
                self.vars[("Variables", self.__name)]["Value"] =\
                    OperatorUtils.apply_assignment_op(
                    self.vars[("Variables", self.__name)]["Value"],
                    self.__op,
                    self.__value)
            else:
                if self.__op == "=":
                    self.vars[("Variables", self.__name)] =\
                        {"Value": self.__value}
                else:
                    # TODO: Error
                    return False
        return True

    def what(self):
        return StepType.ASSIGNMENT
