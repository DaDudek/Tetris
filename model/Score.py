from gameSettings.SizeConstants import *


class Score:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def add_point_for_shape(self, shape):
        squares = shape.get_squares()
        for square in squares:
            self.points += POINTS_FOR_SQUARE

    def add_points_for_row(self):
        self.points += POINTS_FOR_ROW

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points
