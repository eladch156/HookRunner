from json import loads
from App.Logger import Logger
from Hook.Hook import run_hook


class ActionException(Exception):
    pass


class Action():
    def __init__(self, params_json):
        raise NotImplementedError

    @classmethod
    def create(cls, json):
        switch = {
            'Test': TestAction,
            'RunHook': RunHookAction,
        }
        _data = json['Data'] if 'Data' in json else None
        return switch[json['Name']](_data) if json['Name'] in switch else None

    def run(self):
        raise NotImplementedError


class TestAction(Action):
    def __init__(self, params_json):
        self.__logger = Logger("Actions", "TestActions")

    def run(self):
        self.__logger.log("Debug", "Test action is running.")


class RunHookAction(Action):
    def __init__(self, params_json):
        self.__logger = Logger("Actions", "RunHookAction")
        self.__params_json = params_json

    def run(self):
        _hook_path = self._hook_path = self.__params_json['HookPath']
        self.__logger.log("Debug", "Running hook: {}", _hook_path)
        run_hook(_hook_path)
