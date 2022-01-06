from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String

Base = declarative_base()


class Color(Base):
    __tablename__ = 'Color'

    id = Column(Integer, primary_key=True)
    red = Column(Integer, nullable=False)
    green = Column(Integer, nullable=False)
    blue = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    shape = Column(Integer, ForeignKey("Shape.id"))  # check is needed

    def get_red_part(self):
        return self.red

    def get_blue_part(self):
        return self.blue

    def get_green_part(self):
        return self.green

    def get_name(self):
        return self.name


