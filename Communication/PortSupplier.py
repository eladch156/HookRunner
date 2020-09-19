from App.Logger import Logger
import logging
from Utils.General import ComUtils
from Utils.Exceptions import GeneralException,ErrorCodes
import sqlite3
import datetime 

class PortSupplier():
    def __init__(self, port = -1):
        self._logger = Logger("Communication","PortManager")
        self._port = port
        if port != -1:
            self._logger.log(logging.INFO,"Communication Port : {}".format(self._port))
    def save(self):
        dbFileName = ComUtils.getComDbFileByOs()
        self._logger.log(logging.INFO,"Port DB File : {}".format(dbFileName))
        if dbFileName.exists() and dbFileName.stat().st_size > 30 * 1000 :
            dbFileName.unlink()
        connection = sqlite3.connect(dbFileName)
        cursor = connection.cursor()
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PortStorage' ''')
        if cursor.fetchone()[0] == 1: 
            self._logger.log(logging.INFO, "Port Table exists - skip creation.")
        else:
            cursor.execute('''CREATE TABLE PortStorage (Date text, Port integer)''')
        now = datetime.datetime.now()
        cursor.execute("INSERT INTO PortStorage VALUES ('{}','{}')".format(now.strftime("%x %X"),self._port)) 
        connection.commit()
        connection.close()
    def load(self):
        dbFileName = ComUtils.getComDbFileByOs()
        self._logger.log(logging.INFO,"Port DB File : {}".format(dbFileName))
        if not dbFileName.exists():
            raise GeneralException(ErrorCodes.COMMUNICATION_DB_ERROR,"DB File doesn't exist.")
        connection = sqlite3.connect(dbFileName)
        cursor = connection.cursor()
        cursor.execute("SELECT Port FROM PortStorage ORDER BY Date DESC LIMIT 1")
        self._port = cursor.fetchone()[0]
        self._logger.log(logging.INFO,"Found Port : {}".format(self._port))
        connection.close()
        return self._port



        