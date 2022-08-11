# import sys
from time import perf_counter
import pickle
# sys.path.insert(0, '/home/lelet/selenium_linux/')
from extract.preprocessor import clean_table_generator
def unpacking():
    with open('table.pickle', 'rb') as fp:
        table = pickle.load(fp)

    clean_table = clean_table_generator(table)
    return clean_table

if __name__ == '__main__':
        start = perf_counter()
        clean_table = unpacking()
        print(clean_table)
        
        stop = perf_counter()
        print(f'module running in {stop-start:.4f} seconds')