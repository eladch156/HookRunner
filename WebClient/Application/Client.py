from io import StringIO
from socket import socket,AF_INET,SOCK_STREAM
from json import dumps,loads
import atexit
from Utils.General import ComUtils,HOOK_RUNNER_TEMP_PATH
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from Env.EnvSingleton import Environment
from Env.ArgReader import ArgReader

BUFFER_SIZE = 8192

class Client():
    def __init__(self):
        self._enviorment = Environment()
        self._argReader = ArgReader()
        self._argReader.parse()
        self._enviorment.readFromFile()
        self._socket = socket(AF_INET,SOCK_STREAM)
        self._socket.connect(('localhost',int(self._enviorment["port"])))
        atexit.register(self.clean)
    def clean(self):
        self._socket.close()
    def send(self,json):
        try:
            self._socket.send(dumps(json).encode())
        except ValueError as _:
            self._socket.send(json.encode())
    def recv(self):
        return loads(self._socket.recv(BUFFER_SIZE))
        
        
        