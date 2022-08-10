import sys
from time import perf_counter
from db import add_all_homepage
import pickle
sys.path.insert(0, '/home/lelet/selenium_linux/')
from extract.preprocessor import clean_table_generator

def unpacking():
    with open('table.pickle', 'rb') as fp:
        table = pickle.load(fp)

    clean_table = clean_table_generator(table)
    return clean_table


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from decouple import config

    start = perf_counter()
    clean_table_data = unpacking()
    engine = create_engine(config('POSTGRES_URI'), echo=True)
    add_all_homepage(clean_table_data, engine)

    
    stop = perf_counter()
    print(f'module running in {stop-start:.4f} seconds')