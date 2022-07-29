from typing import List
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from decouple import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import NamedTuple

Base = declarative_base()

class User(Base):
    __tablename__ = 'users' # create table users
		
    id:int = Column(Integer, primary_key=True)
    fund:str = Column(String)
    company:str = Column(String)
    fund_type:str = Column(String)
    price:float = Column(Float)
    purchase_time:datetime = Column(DateTime)
    create_at:datetime = Column(DateTime)

    def __repr__(self):
        return f'User {self.name}'

class UserAbstract(NamedTuple):
    fund:str
    company:str
    fund_type:str
    price:float
    purchase_time:datetime
    create_at:datetime = datetime.utcnow() + timedelta(hours=7)

    
def add_user(engine, user:UserAbstract):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_user = User(**asdict(user))
        session.add(new_user)
        session.commit()

    
def add_users(engine, users:List[UserAbstract]):
    Session = sessionmaker(bind=engine)
    user_list = (User(**asdict(user)) for user in users)
    with Session() as session:
        session.bulk_save_objects(user_list)
        session.commit()


if __name__ == '__main__':
    engine = create_engine(config('POSTGRES_URI'), echo=True)
    Base.metadata.create_all(engine)

    