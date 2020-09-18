import logging
import os
from pathlib import Path

WIN_HOOK_RUNNER_TEMP_PATH = Path(os.getenv('APPDATA')) / "HookRunner"
LINUX_HOOK_RUNNER_TEMP_PATH = Path("/var/log/HookRunner")
HOOK_RUNNER_TEMP_PATH=None

if os.name == "nt":
    if not WIN_HOOK_RUNNER_TEMP_PATH.exists():
        WIN_HOOK_RUNNER_TEMP_PATH.mkdir() 
    HOOK_RUNNER_TEMP_PATH = WIN_HOOK_RUNNER_TEMP_PATH
elif os.name == "posix":
    if not LINUX_HOOK_RUNNER_TEMP_PATH.exists():
        LINUX_HOOK_RUNNER_TEMP_PATH.mkdir()
    HOOK_RUNNER_TEMP_PATH = LINUX_HOOK_RUNNER_TEMP_PATH
else:
    raise OSError

class LogUtils():
    
    @classmethod
    def strToLogLevel(cls, strLevel):
        switch = {
            "Debug" : logging.DEBUG,
            "Info" : logging.INFO,
            "Warning" : logging.WARNING,
            "Error" : logging.ERROR
        }
        return logging.INFO if strLevel not in switch else switch[strLevel]

    @classmethod
    def getLogFileByOs(cls):
        return (HOOK_RUNNER_TEMP_PATH / "HookRunner.log")

class ComUtils():
    @classmethod
    def getComDbFileByOs(cls):
        return (HOOK_RUNNER_TEMP_PATH / "HookRunnerComm.db")