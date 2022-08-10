import sys
from time import perf_counter
from db import add_all_additional_info
import pickle
sys.path.insert(0, '/home/lelet/selenium_linux/')
from extract.preprocessor import clean_fund_src

def unpacking():
    with open('returned_table.pickle', 'rb') as fp:
        table = pickle.load(fp)

    clean_src = clean_fund_src(table)
    return clean_src


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from decouple import config

    start = perf_counter()
    clean_src_data = unpacking()
    engine = create_engine(config('POSTGRES_URI'), echo=True)
    add_all_additional_info(clean_src_data, engine)

    
    stop = perf_counter()
    print(f'module running in {stop-start:.4f} seconds')