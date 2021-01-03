import os, datetime, time
import threading

SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))

# This class handles application level log
class LogHandler(object):
    def __init__(self, arg_id: str, arg_log_path: str):
        self._time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self._id = arg_id
        self._log_dir = arg_log_path
        t_timestamp = datetime.datetime.now()
        self._log_full_path = os.path.join(self._log_dir, F'{self._id}_{t_timestamp:%Y%m%d_%H%M%S}.log')

        self._lock = threading.Lock()
        self._retry_limit = 5

        try:
            if not os.path.exists(self._log_dir):
                os.makedirs(self._log_dir)
            self._log_handle = open(self._log_full_path, 'w')
            self.log_message(F'{self._id} starts.')
        except (OSError, IOError) as e:
            raise ValueError(F'Error: Cannot open log file ({self._log_full_path}): {e}')

    def __del__(self):
        self._log_handle.close()

    def log_message(self, arg_message: str) -> None:
        t_timestamp = datetime.datetime.now()
        t_contents = F'{t_timestamp:{self._time_format}}: {arg_message}'
        self._write_log_to_file(t_contents)

    def log_warning(self, arg_message: str) -> None:
        t_timestamp = datetime.datetime.now()
        t_contents = F'{t_timestamp:{self._time_format}}: **WARNING** {arg_message}'
        self._write_log_to_file(t_contents)

    def log_error(self, arg_message: str) -> None:
        t_timestamp = datetime.datetime.now()
        t_contents = F'{t_timestamp:{self._time_format}}: {"*" * 10}ERROR{"*" * 10}\n\t{arg_message}'
        self._write_log_to_file(t_contents)

    def _write_log_to_file(self, arg_contents: str) -> bool:
        self._lock.acquire()
        print(arg_contents)
        self._log_handle.write(arg_contents + '\n')
        self._log_handle.flush()
        self._lock.release()

    def retrieve_log(self):
        fh = open(self._log_full_path, 'r')
        t_log_content = fh.read()
        fh.close()
        return t_log_content