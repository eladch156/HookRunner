from json import loads
from App.Logger import Logger
import logging
from asyncore import ExitNow
from Hook.Hook import runHook

class ActionException(Exception):
    pass

class Action():
    def __init__(self, paramsJson):
        raise NotImplementedError
    @classmethod
    def create(cls, json):
        switch = {
            'Test' : TestAction,
            'RunHook' : RunHookAction,
        }
        data = json['Data'] if 'Data' in json else None
        return switch[json['Name']](data) if json['Name'] in switch else None
    def run(self):
        raise NotImplementedError

class TestAction(Action):
    def __init__(self, paramsJson):
        self._logger = Logger("Actions","TestActions")
    def run(self):
        self._logger.log(logging.DEBUG,"Test action is running.")

class RunHookAction(Action):
    def __init__(self, paramsJson):
        self._logger = Logger("Actions","RunHookAction")
        self._paramsJson = paramsJson
    def run(self):
        hookPath = self._hookPath = self._paramsJson['HookPath']
        self._logger.log(logging.DEBUG,"Running hook: {}", hookPath)
        runHook(hookPath)
        