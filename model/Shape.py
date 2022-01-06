from db.DatabaseSettings import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String


class Shape(Base):
    __tablename__ = "Shape"

    id = Column(Integer, primary_key=True)
    actualPoints = []
    actualRotation = Column(Integer, primary_key=True)
    possibleRotation = []
    color = relationship("Color")

    def get_color(self):
        return self.color

    def get_points(self):
        return self.color

    def get_actual_rotation(self):
        return self.actualRotation

    def get_next_rotation(self):
        return self.possibleRotation[(self.actualRotation+1) % len(self.possibleRotation)]



