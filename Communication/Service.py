import asyncore
from queue import Queue
from threading import Thread
from Communication.Actions import Action
from App.Logger import Logger
import logging
from json import loads
from Utils.Exceptions import AntlrExcption
from Env.EnvSingleton import Environment

TASK_QUEUE = Queue()
BUFFER_SIZE = 8192
IS_FINISH = False

def _handleTasks():
    while True:
        _logger = Logger("Service","TaskHandler")
        try:
            action = Action.create(TASK_QUEUE.get(block=True, timeout=3))
        except Exception as ex:
            if IS_FINISH:
                break
            else:
                continue
        try:
            action.run()
        except AntlrExcption as ex:
            _logger.log(logging.ERROR,str(ex))
        _logger.log(logging.INFO,"Task is done...")
        TASK_QUEUE.task_done()
        _logger.log(logging.INFO,"Waiting for the next task...")
    if IS_FINISH:
        _logger.log(logging.DEBUG,"Main thread signed to exit.")

class ServiceThread(Thread):
    def __init__(self, host):
        global IS_FINISH
        Thread.__init__(self)
        self._logger = Logger("Service","MainThread")
        self._service = Service(host)
        IS_FINISH = False
        self._taskHandler = Thread(target=_handleTasks)
    def run(self):
        self._taskHandler.start()
        asyncore.loop()
    def stop(self):
        global IS_FINISH
        IS_FINISH = True
        self._taskHandler.join()
        self._logger.log(logging.DEBUG,"Closing all connections...")
        asyncore.close_all()
        self._logger.log(logging.DEBUG,"Waiting for service dispatcher to close...")
        self._service.close()
        self._logger.log(logging.DEBUG,"Service dispatcher closed...")
        self.join()

class ServiceHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        buffer = self.recv(BUFFER_SIZE)
        if buffer:
            data = loads(buffer.decode("UTF-8"))
            TASK_QUEUE.put(data,block=True,timeout=5)

class Service(asyncore.dispatcher):
    def __init__(self,host):
        asyncore.dispatcher.__init__(self)
        self._logger = Logger("Service","Dispatcher")
        self.create_socket()
        self.set_reuse_addr()
        self._env = Environment()
        self.bind((host,int(self._env["port"])))
        self.listen(5)
    def handle_close(self):
        self._logger.log(logging.DEBUG,"Client: Connection Closed") 
    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            self._logger.log(logging.DEBUG,"Incoming request : {}",repr(addr))
            handler = ServiceHandler(sock=sock)

