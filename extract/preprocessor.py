from typing import List, TypedDict
from datetime import datetime
import re

class TableDataInterface(TypedDict):
    fund: str
    company: str
    fund_type: str
    price: float
    update_at: datetime

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
                price, purchase_time = value.split('Cập nhật ngày')
                price = float(price.replace(',', ''))
                purchase_time = datetime.strptime(purchase_time.strip()+'/'+str(datetime.now().year), '%d/%m/%Y')
                dict_i['price'] = price
                dict_i['purchase_time'] = purchase_time
        result_list.append(dict_i)

    return result_list

def parse_fund_page_src(page_src):
    lines = []
    for i in page_src:
        lines.append(i.text)
    return lines

def clean_fund_src(returned_table):
    dict_page_src = {i: parse_fund_page_src(returned_table[i]) for i in returned_table.keys()}
    result_dict = {}
    for index, value in dict_page_src.items():
        place_order, conversion_fee = value[4:6]
        splitted_place_order = ' '.join(place_order[33:].split(' ngày '))
        place_order = datetime.strptime(splitted_place_order, '%H:%M %d/%m/%Y')
        if len(conversion_fee) > 0:
            number_found = re.findall("\d+\.\d+|\d+", conversion_fee)[0]
            conversion_fee = float(number_found)
        else:
            conversion_fee = 0
        result_dict[index] = (place_order, conversion_fee)

    return result_dict
