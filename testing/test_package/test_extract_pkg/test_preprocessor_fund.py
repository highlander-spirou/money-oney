from time import perf_counter
import pickle
from extract.preprocessor import clean_fund_src
def unpacking():
    with open('returned_table.pickle', 'rb') as fp:
        table = pickle.load(fp)

    clean_table = clean_fund_src(table)
    return clean_table

if __name__ == '__main__':
        start = perf_counter()
        clean_table = unpacking()
        print(clean_table)
        
        stop = perf_counter()
        print(f'module running in {stop-start:.4f} seconds')