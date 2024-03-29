import os, sys, datetime

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import data_scraper.ds_cme
import tools.utilities

def run_data_scraper(arg_logger, arg_data_dir):
    cme_scraper = data_scraper.ds_cme.DataScraperCME(arg_logger, arg_data_dir)
    t_today = datetime.date.today()
    for i in range(7):
        arg_logger.log_message(F'To download CME files for {t_today: %Y-%m-%d}')
        cme_scraper.scrape_data(datetime.date(t_today.year, t_today.month, t_today.day))
        t_today += datetime.timedelta(days=-1)

def main():
    t_logger = tools.utilities.LogHandler('controller_ds', '~/Documents/projects/Log')
    t_data_dir = '~/Documents/projects/Data'
    run_data_scraper(t_logger, t_data_dir)

if __name__ == "__main__":
    main()