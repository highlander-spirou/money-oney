from db.schemas import AdditionalInfoFactory, HomePageTableFactory
from time import perf_counter


if __name__ == '__main__':
    from datetime import datetime
    start = perf_counter()
    prime = ('VESAF', 'VINA', 'ck', 10.00, datetime(2022, 2, 2, 13, 25), )
    primer = ('VESAF', datetime(2022, 2, 2, 13, 25), 0.0)

    a = HomePageTableFactory(*prime)
    c = AdditionalInfoFactory(*primer)

    print(a)
    print(c)
    stop = perf_counter()
    print(f'module running in {stop-start:.4f} seconds')
