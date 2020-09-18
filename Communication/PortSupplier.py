from App.Logger import Logger
import logging
from Utils.General import ComUtils
import sqlite3
import datetime 

class PortSupplier():
    def __init__(self, port):
        self._logger = Logger("Communication","PortManager")
        self._port = port
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
