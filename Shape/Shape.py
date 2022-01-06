from model.Point import Point
from gameSettings.SizeConstants import *


class Shape:
    def __init__(self, shapeTemplate):
        self.upper_left_square = Point(INIT_WIGHT/2, 0)
        self.actualRotation = 0
        self.shapeTemplate = shapeTemplate  # shape template

    def get_coordinate(self):
        return self.upper_left_square

    def get_actual_rotation(self):
        return self.shapeTemplate.get_rotation(self.actualRotation)

    def get_next_rotation(self):
        self.actualRotation = (self.actualRotation + 1) % 4
        return self.get_actual_rotation()

    def get_color(self):
        return self.shapeTemplate.color.get_color()

    def set_coordinate(self, coordinate):
        self.upper_left_square = coordinate



