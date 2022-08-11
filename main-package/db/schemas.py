from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from typing import NamedTuple

Base = declarative_base()

class Table(Base):
    __tablename__ = 'homepageTable'

    id:int = Column(Integer, primary_key=True)
    fund:str = Column(String)
    company:str = Column(String)
    fund_type:str = Column(String)
    price:float = Column(Float)
    price_updated_at:datetime = Column(DateTime)
    create_at:datetime = Column(DateTime)


class AdditionalInfo(Base):
    __tablename__ = 'infoTable'

    id:int = Column(Integer, primary_key=True)
    fund:str = Column(String)
    place_order_time:datetime = Column(DateTime)
    conversion_fee:float = Column(Float)
    create_at:datetime = Column(DateTime)


class HomePageTableFactory(NamedTuple):
    fund:str
    company:str
    fund_type:str
    price:float
    price_updated_at:datetime
    create_at:datetime = datetime.utcnow() + timedelta(hours=7)

class AdditionalInfoFactory(NamedTuple):
    fund:str
    place_order_time:datetime
    conversion_fee:float
    create_at:datetime = datetime.utcnow() + timedelta(hours=7)

