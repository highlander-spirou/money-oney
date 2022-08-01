import sys
from time import perf_counter
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
if __name__ == '__main__':
    sys.path.insert(0, '/home/lelet/selenium_linux/')
    import pickle
    from extract.preprocessor import *
    start = perf_counter()
    with open(f'{ROOT_DIR}/cache/table.pickle', 'rb') as fp:
        table = pickle.load(fp)
    with open(f'{ROOT_DIR}/cache/returned_table.pickle', 'rb') as fp:
        returned_table = pickle.load(fp)

    print(clean_table_generator(table))
    print(clean_fund_src(returned_table))
    stop = perf_counter()
    print(f'module running in {stop-start:.4f} seconds')