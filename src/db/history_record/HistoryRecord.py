from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///main.db", echo=False)  # change for true to have logs


class HistoryRecord(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    points = Column(Integer, nullable=False)
    player_name = Column(String, nullable=False)

    def get_points(self) -> int:
        return self.points

    def get_player_name(self) -> str:
        return self.player_name

    def __str__(self) -> str:
        return f"{self.player_name} {self.points}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


def get_session() -> Session:
    return session
