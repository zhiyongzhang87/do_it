import os, datetime
import ftplib
from enum import Enum

class CMEFileCategory(Enum):
    Settle = 1
    SPAN = 2

class DataScraperCME(object):
    def __init__(self, arg_logger):
        self._logger = arg_logger
        self._url = 'ftp.cmegroup.com'
        self._ftp_path_settle = 'settle'
        self._ftp_path_span = 'pub/span/data'
        self._ftp_handle = None

    def scrape_data(self, arg_date: datetime.date = datetime.date.today()) -> None:
        t_file_name_settle = F'settle.{arg_date.strftime("%Y%m%d")}.s.xml.zip'

        self._connect_ftp()
        self._download_file_from_ftp(self._ftp_path_settle, t_file_name_settle)

    def _connect_ftp(self) -> None:
        self._ftp_handle = ftplib.FTP(self._url)
        self._ftp_handle.login()

    def _download_file_from_ftp(self, arg_ftp_path: str, arg_file_name: str, arg_local_path: str) -> None:
        # Set ftp handle to root directory
        self._ftp_handle.cwd('/')

        # Verify arg_ftp_path
        t_path_folders = arg_ftp_path.split('/')
        for t_path_folder in t_path_folders:
            t_listed_folders = self._ftp_handle.mlsd()
            if t_path_folders not in t_listed_folders:
                self._logger.log_error(F'Cannot find FTP path {arg_ftp_path}! Download failed.')
                break
            self._ftp_handle.cwd(t_path_folder)

        # Download files with arg_file_name in file name
        t_listed_files = self._ftp_handle.mlsd()
        for t_file_name in t_listed_files:
            if arg_file_name in t_file_name:
                t_local_full_path = os.path.join(arg_local_path, t_file_name)
                with open(t_local_full_path, 'w') as t_local_file_handle:
                    t_result = self._ftp_handle.retrbinary(F'RETR {t_file_name}', t_local_file_handle.write)
                    if not t_result.startswith('226 Transfer complete'):
                        self._logger.log_error(F'Download {t_file_name} failed.')
            
            