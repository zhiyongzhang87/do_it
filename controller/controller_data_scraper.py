import os, sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import data_scraper.ds_cme

def run_data_scraper():
    cme_scraper = data_scraper.ds_cme.DataScraperCME()
    cme_scraper.scrape_data()

def main():
    run_data_scraper()

if __name__ == "__main__":
    main()