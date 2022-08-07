from decouple import config
import sys
sys.path.insert(0, '/home/lelet/selenium_linux/')

from extract.crawler import *
from extract.preprocessor import *

def run_extraction():
    url = config('SCRAPES_URL')
    table, returned_table = run_crawler(url)
    clean_table = clean_table_generator(table)
    clean_fund = clean_fund_src(returned_table)

    return clean_table, clean_fund