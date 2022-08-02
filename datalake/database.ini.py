import sys
if __name__ == '__main__':
    sys.path.insert(0, '/home/lelet/selenium_linux/')
    from sqlalchemy import create_engine, inspect
    from decouple import config
    from datalake.tables import Base
    engine = create_engine(config('POSTGRES_URI'), echo=False)
    inspector = inspect(engine)
    meta_tables = {i for i in Base.metadata.tables.keys()}
    remote_tables = set(inspector.get_table_names())
    if len(meta_tables - remote_tables) > 0:
        Base.metadata.create_all(engine)
        print('All base engine has been created')

    

