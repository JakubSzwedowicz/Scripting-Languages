# Author: Jakub Szwedowicz
# Date: 12.05.2022
# e-mail: kuba.szwedowicz@gmail.com

from datetime import datetime
from enum import Enum


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=_Singleton):
    class Level(Enum):
        INFO = 1
        WARNING = 2
        ERROR = 3

    DEFAULT_FILENAME = 'default_log.txt'

    def __init__(self, print_to_console: bool = False, filename: str = DEFAULT_FILENAME):
        self._filename = filename
        self._debug_mode = print_to_console
        self._file_handle = None
        self.set_logger_file(filename)

    def __del__(self):
        self._file_handle.close()

    def set_logger_file(self, filename: str) -> None:
        if self._file_handle and not self._file_handle.closed:
            self._file_handle.close()

        try:
            self._filename = filename
            self._file_handle = open(filename, 'w+')
            self.log_info(f'Created a new file for the logger "{filename}"')
        except IOError as ex:
            self._file_handle = None
            print(f'Logger not initialized! Cannot create a file {self._filename}, error {ex}')

    def log_info(self, msg: str) -> None:
        self._log_msg(msg, Logger.Level.INFO)

    def log_warn(self, msg: str) -> None:
        self._log_msg(msg, Logger.Level.WARNING)

    def log_error(self, msg: str) -> None:
        self._log_msg(msg, Logger.Level.ERROR)

    def _log_msg(self, msg: str, level: Level) -> None:
        if not self._file_handle:
            print(f'Logger not initialized! Cannot log the message!!!')

        try:
            formatted_msg = self._format_msg(msg, level)
            self._file_handle.write(formatted_msg)
            if self._debug_mode:
                print(formatted_msg)
        except IOError as ex:
            print(f'Logger cannot save message to the file {self._filename}, error {ex}')

    @staticmethod
    def _format_msg(msg: str, level: Level) -> str:
        time = datetime.now().strftime("%H:%M:%S")
        return f"[{time}][{level.name}] {msg}\n"



