from typing import List
from sqlalchemy.orm import sessionmaker
from datalake.tables import *
class TableInterface:
    pass

class RowInterface:
    pass


def add_row(engine, table:TableInterface, row:RowInterface):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_user = table(**row._asdict())
        session.add(new_user)
        session.commit()

    
def add_rows(engine, table:TableInterface ,rows:List[RowInterface]):
    Session = sessionmaker(bind=engine)
    user_list = (table(**row._asdict()) for row in rows)
    with Session() as session:
        session.bulk_save_objects(user_list)
        session.commit()

def add_all_homepage(clean_table_data, engine):
    added_data = (HomePageTableFactory(**i) for i in clean_table_data)
    add_rows(engine, Table, added_data)

def add_all_additional_info(clean_src_data, engine):
    added_data = (AdditionalInfoFactory(*i) for i in clean_src_data)
    add_rows(engine, AdditionalInfo, added_data)
