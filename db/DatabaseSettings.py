from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///main.db", echo=False)  # change for true to have logs
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

