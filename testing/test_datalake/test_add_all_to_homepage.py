import sys
from time import perf_counter
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
if __name__ == '__main__':
        sys.path.insert(0, '/home/lelet/selenium_linux/')
        from datalake.utils import add_all_homepage
        from testing.test_crawler.preprocessor_ import preprocessor_test_module
        from sqlalchemy import create_engine
        from decouple import config

        start = perf_counter()
        clean_table_data, _ = preprocessor_test_module()
        engine = create_engine(config('POSTGRES_URI'), echo=True)
        add_all_homepage(clean_table_data, engine)

        
        stop = perf_counter()
        print(f'module running in {stop-start:.4f} seconds')