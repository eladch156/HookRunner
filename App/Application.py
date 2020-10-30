from Env.ArgReader import ArgReader
from Env.EnvSingleton import Environment
from App.Logger import Logger
from HookLibs.CommadLibrary import LibsSingleton
from Communication.Service import ServiceThread
import asyncore


class Application():
    def __init__(self):
        self.__enviorment = Environment()
        self.__arg_reader = ArgReader()
        self.__arg_reader.parse()
        self.__enviorment.read()

    def run(self):
        self.__lib_spec_reader = LibsSingleton()
        self.__logger = Logger("Application")
        self.__logger.log("Info", "HookRunner is running.")
        self.__lib_spec_reader.init()
        self.__service = ServiceThread('localhost')
        self.__service.start()
        self.__logger.log("Info", "Server is ready...")
        self.__logger.log("Info",
                          "Is ServerThread alive?"
                          " {status}".format(status=str(
                                    self.__service.is_alive())))
        self.__logger.log("Info", "On any input server will close.")
        dummy = input()
        self.__service.stop()
