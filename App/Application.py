from Env.ArgReader import ArgReader
from Env.EnvSingleton import Environment
from App.Logger import Logger
from HookLibs.CommadLibrary import LibsSingleton
import logging
from Communication.Service import ServiceThread
import asyncore

class Application():
    def __init__(self):
        self._enviorment = Environment()
        self._argReader = ArgReader()
        self._argReader.parse()
        self._enviorment.readFromFile()
    def run(self): 
        self._libSpecReader = LibsSingleton()
        self._logger = Logger("Application")
        self._logger.log(logging.INFO,"HookRunner is running.")
        self._libSpecReader.init()
        self._service = ServiceThread('localhost')
        self._service.start()
        self._logger.log(logging.INFO, "Server is ready...")
        self._logger.log(logging.DEBUG, "Is ServerThread alive? {status}".format(status=str(self._service.is_alive())))
        self._logger.log(logging.INFO,"On any input server will close.")
        dummy = input()
        self._service.stop()

