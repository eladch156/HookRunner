from io import StringIO
from socket import socket, AF_INET, SOCK_STREAM
from json import dumps, loads
import atexit
from Utils.General import HOOK_RUNNER_TEMP_PATH
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from Env.EnvSingleton import Environment
from Env.ArgReader import ArgReader

BUFFER_SIZE = 8192


class Client():
    def __init__(self):
        self.__enviorment = Environment()
        self.__arg_reader = ArgReader()
        self.__arg_reader.parse()
        self.__enviorment.read()
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.connect(('localhost', int(self.__enviorment["port"])))
        atexit.register(self.clean)

    def clean(self):
        self.__socket.close()

    def send(self, json):
        try:
            self.__socket.send(dumps(json).encode())
        except ValueError as _:
            self.__socket.send(json.encode())

    def recv(self):
        return loads(self.__socket.recv(BUFFER_SIZE))
