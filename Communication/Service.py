import asyncore
from queue import Queue
from threading import Thread
from Actions import Action
from App import Logger
import logging
from json import loads

TASK_QUEUE = Queue()
BUFFER_SIZE = 8192
LoggerSingleton = Logger.Logger()

def _handleTasks():
    while True:
        LoggerSingleton.log(logging.INFO,"Waiting for the next task...")
        action = Action.create(TASK_QUEUE.get())
        action.run()
        LoggerSingleton.log(logging.INFO,"Task is done...")
        TASK_QUEUE.task_done()

class ServiceHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = loads(self.recv(BUFFER_SIZE))
        TASK_QUEUE.put(data)

class Service(asyncore.dispatcher):
    def __init__(self,host):
        asyncore.dispatcher.__init__(self)
        Thread(target=_handleTasks).start()
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host,0))
        self.listen(5)
    def handle_accept(self, sock, addr):
        LoggerSingleton.log(logging.DEBUG,"Incoming request , (Address: %s)",repr(addr))
        handler = ServiceHandler(sock=sock)

