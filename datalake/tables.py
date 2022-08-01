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
    purchase_time:datetime = Column(DateTime)
    create_at:datetime = Column(DateTime)

    def __repr__(self):
        return f'User {self.name}'

class HomePageTableFactory(NamedTuple):
    fund:str
    company:str
    fund_type:str
    price:float
    purchase_time:datetime
    create_at:datetime = datetime.utcnow() + timedelta(hours=7)

