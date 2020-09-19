from Communication.PortSupplier import PortSupplier
from io import StringIO
from socket import socket,AF_INET,SOCK_STREAM
from json import dumps,loads
import atexit

BUFFER_SIZE = 8192

class Client():
    def __init__(self):
        self._port = PortSupplier().load()
        self._scocket = socket(AF_INET,SOCK_STREAM)
        self._scocket.connect(('localhost',self._port))
        atexit.register(self._scocket.close)
    def send(self,json):
        try:
            self._scocket.send(dumps(json).encode())
        except ValueError as _:
            self._scocket.send(json.encode())
    def recv(self):
        return loads(self._scocket.recv(BUFFER_SIZE))
        
        