import logging
import os
from pathlib import Path

WIN_HOOK_RUNNER_TEMP_PATH = Path(os.getenv('APPDATA')) / "HookRunner"
LINUX_HOOK_RUNNER_TEMP_PATH = Path("/var/log/HookRunner")
HOOK_RUNNER_TEMP_PATH = None

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
    def str_to_log_level(cls, str_level):
        switch = {
            "Debug": logging.DEBUG,
            "Info": logging.INFO,
            "Warning": logging.WARNING,
            "Error": logging.ERROR
        }
        return switch.get(str_level, logging.INFO)

    @classmethod
    def get_log_file_by_os(cls):
        return (HOOK_RUNNER_TEMP_PATH / "HookRunner.log")
