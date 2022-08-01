import sys
from datetime import datetime
from sqlalchemy import create_engine
from decouple import config
if __name__ == '__main__':
    sys.path.insert(0, '/home/lelet/selenium_linux/')
    from datalake.utils import *
    from datalake.tables import HomePageTableFactory, Table
    
    a = HomePageTableFactory(**{'fund': 'VESAF', 'company': 'VINACAPITAL', 'fund_type': 'Quỹ cổ phiếu', 'price': 23957.98, 'price_updated_at': datetime(2022, 8, 1, 0, 0)})
    b = HomePageTableFactory(**{'fund': 'VFF', 'company': 'VINACAPITAL', 'fund_type': 'Quỹ trái phiếu', 'price': 19996.06, 'price_updated_at': datetime(2022, 7, 28, 0, 0)})
    c = HomePageTableFactory(**{'fund': 'VLGF', 'company': 'SSIAM', 'fund_type': 'Quỹ cổ phiếu', 'price': 9440.09, 'price_updated_at': datetime(2022, 8, 1, 0, 0)})
    
    engine = create_engine(config('POSTGRES_URI'), echo=True)
    add_row(engine, Table, a)
    add_rows(engine, Table, [b, c])