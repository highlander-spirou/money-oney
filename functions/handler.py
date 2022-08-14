from decouple import config
from sqlalchemy import create_engine

from extract.crawler import run_crawler
from extract.preprocessor import clean_table_generator, clean_fund_src
from db import add_all_additional_info, add_all_homepage

url = config('SCRAPES_URL')
db_uri = config('POSTGRES_URI')

def run():
    dirty_table, dirty_fund_src = run_crawler(url)
    clean_table = clean_table_generator(dirty_table)
    clean_fund = clean_fund_src(dirty_fund_src)

    engine = create_engine(db_uri)
    add_all_homepage(clean_table, engine)
    add_all_additional_info(clean_fund, engine)


if __name__ == '__main__':
    run()