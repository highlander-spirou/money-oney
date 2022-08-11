from typing import List, TypedDict
from datetime import datetime
import re

class TableDataInterface(TypedDict):
    fund: str
    company: str
    fund_type: str
    price: float
    price_updated_at: datetime

def clean_table_generator(table_gen) -> List[TableDataInterface]:
    result_list = []
    for i in table_gen:
        dict_i: TableDataInterface = {}
        for index, value in enumerate(i):
            if index == 0:
                dict_i['fund'] = value
            elif index == 1:
                dict_i['company'] = value
            elif index == 2:
                dict_i['fund_type'] = value
            elif index == 3:
                price, price_updated_at = value.split('Cập nhật ngày')
                price = float(price.replace(',', ''))
                price_updated_at = datetime.strptime(price_updated_at.strip()+'/'+str(datetime.now().year), '%d/%m/%Y')
                dict_i['price'] = price
                dict_i['price_updated_at'] = price_updated_at
        result_list.append(dict_i)

    return result_list

def parse_fund_page_src(page_src):
    lines = []
    for i in page_src:
        lines.append(i.text)
    return lines

def clean_fund_src(returned_table):
    dict_page_src = {i: parse_fund_page_src(returned_table[i]) for i in returned_table.keys()}
    result_list = []
    for index, value in dict_page_src.items():
        place_order_time, conversion_fee = value[4:6]
        splitted_place_order_time = ' '.join(place_order_time[33:].split(' ngày '))
        place_order_time = datetime.strptime(splitted_place_order_time, '%H:%M %d/%m/%Y')
        if len(conversion_fee) > 0:
            number_found = re.findall("\d+\.\d+|\d+", conversion_fee)[0]
            conversion_fee = float(number_found)
        else:
            conversion_fee = 0
        result_list.append((index, place_order_time, conversion_fee))

    return result_list
