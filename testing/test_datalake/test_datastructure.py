import sys
from time import perf_counter
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
if __name__ == '__main__':
        sys.path.insert(0, '/home/lelet/selenium_linux/')
        from datetime import datetime
        from datalake.tables import AdditionalInfoFactory
        start = perf_counter()
        primer = ('VESAF', datetime(2022, 2, 2, 13, 25), 0.0)
        c = AdditionalInfoFactory(*primer)
        print(c)
        stop = perf_counter()
        print(f'module running in {stop-start:.4f} seconds')