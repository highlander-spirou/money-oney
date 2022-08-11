from db.schemas import *
from db.utils import *

def add_all_homepage(clean_table_data, engine):
    added_data = (HomePageTableFactory(**i) for i in clean_table_data)
    add_rows(engine, Table, added_data)

def add_all_additional_info(clean_src_data, engine):
    added_data = (AdditionalInfoFactory(*i) for i in clean_src_data)
    add_rows(engine, AdditionalInfo, added_data)