import sys
from time import perf_counter
from pathlib import Path
import pickle
sys.path.insert(0, '/home/lelet/selenium_linux/')

from extract.preprocessor import *
ROOT_DIR = Path(__file__).parent.parent

def preprocessor_test_module():
    with open(f'{ROOT_DIR}/cache/table.pickle', 'rb') as fp:
            table = pickle.load(fp)
    with open(f'{ROOT_DIR}/cache/returned_table.pickle', 'rb') as fp:
        returned_table = pickle.load(fp)

    clean_table = clean_table_generator(table)
    clean_fund = clean_fund_src(returned_table)

    return clean_table, clean_fund

if __name__ == '__main__':
    
    start = perf_counter()
    
    a, b = preprocessor_test_module()
    print(a)
    print(b)
    stop = perf_counter()
    print(f'module running in {stop-start:.4f} seconds')