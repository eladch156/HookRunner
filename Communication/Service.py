import asyncore
from queue import Queue
from threading import Thread
from Communication.Actions import Action
from App.Logger import Logger
from json import loads
from Utils.Exceptions import AntlrExcption
from Env.EnvSingleton import Environment

TASK_QUEUE = Queue()
BUFFER_SIZE = 8192
IS_FINISH = False


def _handle_tasks():
    while True:
        __logger = Logger("Service", "TaskHandler")
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
            __logger.log(logging.ERROR, str(ex))
        __logger.log("Info", "Task is done...")
        TASK_QUEUE.task_done()
        __logger.log("Info", "Waiting for the next task...")
    if IS_FINISH:
        __logger.log("Debug", "Main thread signed to exit.")


class ServiceThread(Thread):
    def __init__(self, host):
        global IS_FINISH
        Thread.__init__(self)
        self.__logger = Logger("Service", "MainThread")
        self.__service = Service(host)
        IS_FINISH = False
        self.__task_handler = Thread(target=_handle_tasks)

    def run(self):
        self.__task_handler.start()
        asyncore.loop()

    def stop(self):
        global IS_FINISH
        IS_FINISH = True
        self.__task_handler.join()
        self.__logger.log("Debug", "Closing all connections...")
        asyncore.close_all()
        self.__logger.log("Debug", "Waiting for service"
                                   " dispatcher to close...")
        self.__service.close()
        self.__logger.log("Debug", "Service dispatcher closed...")
        self.join()


class ServiceHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        buffer = self.recv(BUFFER_SIZE)
        if buffer:
            data = loads(buffer.decode("UTF-8"))
            TASK_QUEUE.put(data, block=True, timeout=5)


class Service(asyncore.dispatcher):
    def __init__(self, host):
        asyncore.dispatcher.__init__(self)
        self.__logger = Logger("Service", "Dispatcher")
        self.create_socket()
        self.set_reuse_addr()
        self.__env = Environment()
        self.bind((host, int(self.__env["port"])))
        self.listen(5)

    def handle_close(self):
        self.__logger.log("Debug", "Service: Connection Closed")

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            self.__logger.log("Debug", "Incoming request"
                                       ": {}", repr(addr))
            handler = ServiceHandler(sock=sock)
