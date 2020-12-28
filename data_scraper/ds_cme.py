import os, datetime
import ftplib
import re
from enum import Enum

class CMEFileCategory(Enum):
    Settle = 1
    SPAN = 2

class DataScraperCME(object):
    def __init__(self, arg_logger, arg_data_dir):
        self._logger = arg_logger
        self._data_dir = arg_data_dir
        self._url = 'ftp.cmegroup.com'
        self._ftp_handle = None

        self._dict_file_category = {}

        self._dict_file_category[CMEFileCategory.Settle] = {}
        self._dict_file_category[CMEFileCategory.Settle]['ftp_path'] = 'settle'
        self._dict_file_category[CMEFileCategory.Settle]['data_dir'] = os.path.join(self._data_dir, 'cme_settle')
        self._dict_file_category[CMEFileCategory.Settle]['file_name_format'] = 'settle.{date}.s.xml.zip'

            # self._ftp_path_span = 'pub/span/data'

    def scrape_data(self, arg_date: datetime.date = datetime.date.today()) -> bool:
        if not self._connect_ftp():
            return False

        for t_file_type in self._dict_file_category:
            try:
                t_data_dir = self._dict_file_category[t_file_type]['data_dir']
                if not os.path.exists(t_data_dir):
                    os.makedirs(t_data_dir)
            except OSError as e:
                self._logger.log_error(F'Create data folder ({t_data_dir}) failed: {e}')
                return False

            t_file_name = re.sub('{date}', F'{arg_date:%Y%m%d}', self._dict_file_category[t_file_type]['file_name_format'])
            self._download_file_from_ftp(self._dict_file_category[t_file_type]['ftp_path'], t_file_name, t_data_dir)

    def _connect_ftp(self) -> bool:
        try:
            self._ftp_handle = ftplib.FTP(self._url)
            self._ftp_handle.login()
        except ftplib.all_errors as e:
            self._logger.log_error(F'{self._url} login failed: {e}')
            return False

        return True

    def _download_file_from_ftp(self, arg_ftp_path: str, arg_file_name: str, arg_local_path: str) -> None:
        # Set ftp handle to root directory
        self._ftp_handle.cwd('/')

        # Verify arg_ftp_path
        t_path_folders = arg_ftp_path.split('/')
        for t_path_folder in t_path_folders:
            t_listed_items = self._ftp_handle.nlst()
            if t_path_folder not in t_listed_items:
                self._logger.log_error(F'Cannot find FTP path {arg_ftp_path}! Download failed.')
                break
            self._ftp_handle.cwd(t_path_folder)

        # Download files with arg_file_name in file name
        t_listed_items = self._ftp_handle.nlst()
        for t_item_name in t_listed_items:
            if arg_file_name in t_item_name:
                t_local_full_path = os.path.join(arg_local_path, t_item_name)
                with open(t_local_full_path, 'wb') as t_local_file_handle:
                    t_result = self._ftp_handle.retrbinary(F'RETR {t_item_name}', t_local_file_handle.write)
                    if not t_result.startswith('226 Transfer complete'):
                        self._logger.log_error(F'Download {t_item_name} failed.')
                    else:
                        self._logger.log_message(F'Download is completed: {t_local_full_path}')
            
            