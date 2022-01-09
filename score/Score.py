from gameSettings.PointsConstants import *
from score.ScoreBonusCalculator import add_points_for_speed, add_points_for_row_numbers


class Score:
    def __init__(self, name, speed, points=0):
        self.name = name
        self.points = points
        self.speed = speed

    def add_point_for_shape(self, shape):
        squares = shape.get_squares()
        for square in squares:
            self.points += POINTS_FOR_SQUARE
        self.points += add_points_for_speed(self.speed)

    def add_points_for_row(self):
        self.points += POINTS_FOR_ROW

    def add_points_for_row_bonus(self, row_number):
        self.points += add_points_for_row_numbers(row_number)

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points
