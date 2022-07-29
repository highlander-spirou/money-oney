from datetime import datetime
from sqlalchemy import create_engine
from decouple import config
from datalake import add_user, UserAbstract

# engine = create_engine(config('POSTGRES_URI'), echo=True)
# add_user(engine, UserAbstract('VESAF', 'VINACAPITAL', 'quỹ chủ động', 23000, datetime(2022, 28, 7, 19, 59)))

user1 = UserAbstract('VESAF', 'VINACAPITAL', 'quỹ chủ động', 23000, datetime(2022, 28, 7, 19, 59))
print(user1.create_at)