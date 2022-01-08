from gameSettings.SizeConstants import *

class Score:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def add_point_for_shape(self, shape):
        squares = shape.get_squares()
        for square in squares:
            self.score += POINTS_FOR_SQUARE

    def add_points_for_row(self):
        self.score += POINTS_FOR_ROW