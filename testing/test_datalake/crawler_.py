import sys
from time import perf_counter
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
if __name__ == '__main__':
        sys.path.insert(0, '/home/lelet/selenium_linux/')
        import pickle
        from extract.crawler import *
        start = perf_counter()
        url = r'https://fmarket.vn/san_pham?search=CHUNG_CHI_QUY-YWxs'
        table, returned_table = run_crawler(url)
        with open(f'{ROOT_DIR}/cache/table.pickle', 'wb') as cache_file:
                pickle.dump(table, cache_file)
        with open(f'{ROOT_DIR}/cache/returned_table.pickle', 'wb') as cache_file:
                pickle.dump(returned_table, cache_file)
        
        stop = perf_counter()
        print(f'module running in {stop-start:.4f} seconds')