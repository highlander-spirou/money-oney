from extract.crawler import run_crawler
from extract.preprocessor import clean_fund_src, clean_table_generator

if __name__ == '__main__':
    # url = r'https://fmarket.vn/san_pham?search=CHUNG_CHI_QUY-YWxs'
    # table, returned_table = run_crawler(url)
    # print(clean_table_generator(table))
    # print(clean_fund_src(returned_table))

    from datetime import datetime
    from decouple import config
    from datalake import UserAbstract, add_users

    from sqlalchemy import create_engine
    engine = create_engine(config('POSTGRES_URI'), echo=True)
    user1 = UserAbstract('DCDS', 'DragonCapital', 'quỹ cân bằng', 23000, datetime(2022, 7, 28, 19, 59))
    user2 = UserAbstract('VEOF', 'VINACAPITAL', 'quỹ chủ động', 33000, datetime(2022, 7, 29, 1, 20))
    add_users(engine, [user1, user2])


