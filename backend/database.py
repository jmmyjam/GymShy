from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:123456789@localhost:5433/gymmy"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)