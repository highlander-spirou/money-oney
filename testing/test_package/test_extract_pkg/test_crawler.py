# import sys
from time import perf_counter
# sys.path.insert(0, '/home/lelet/selenium_linux/')

if __name__ == '__main__':
        import pickle
        from extract.crawler import run_crawler
        start = perf_counter()
        url = r'https://fmarket.vn/san_pham?search=CHUNG_CHI_QUY-YWxs'
        table, returned_table = run_crawler(url)
        with open(f'table.pickle', 'wb') as cache_file:
                pickle.dump(table, cache_file)
        with open(f'returned_table.pickle', 'wb') as cache_file:
                pickle.dump(returned_table, cache_file)
        
        stop = perf_counter()
        print(f'module running in {stop-start:.4f} seconds')