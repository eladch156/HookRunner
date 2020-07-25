from Env.ArgReader import ArgReader
from Env.EnvSingleton import Environment
from App.Logger import Logger
from HookLibs.CommadLibrary import LibsSingleton
import logging
from Communication import Service
import asyncore

class Application():
    def __init__(self):
        self._argReader = ArgReader()
        self._enviorment = Environment()
        self._libSpecReader = LibsSingleton()
        self._logger = None
        self._service = Service.Service('localhost')
    def run(self): 
        self._argReader.parse()
        self._enviorment.readFromFile()
        self._logger = Logger()
        self._logger.log(logging.INFO,"HookRunner is running.")
        self._libSpecReader.init()
        asyncore.loop()
        
