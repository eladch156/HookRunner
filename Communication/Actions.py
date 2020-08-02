from json import loads
from App.Logger import Logger
import logging
from asyncore import ExitNow

class ActionException(Exception):
    pass

class Action():
    def __init__(self):
        raise NotImplementedError
    @classmethod
    def create(cls, json):
        switch = {
            'Test' : TestAction,
        }
        return switch[json['Name']]() if json['Name'] in switch else None
    def run(self):
        raise NotImplementedError

class TestAction(Action):
    def __init__(self):
        self._logger = Logger()
    def run(self):
        self._logger.log(logging.DEBUG,"Test action is running.")