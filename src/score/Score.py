from src.Shape.Shape import Shape
from src.Speed.Speed import Speed
from src.gameSettings.PointsConstants import *
from src.score.ScoreBonusCalculator import add_points_for_speed, add_points_for_row_numbers


class Score:
    def __init__(self, name: str, speed: Speed, points: int = 0):
        self.name = name
        self.points = points
        self.speed = speed

    def add_point_for_shape(self, shape: Shape) -> None:
        squares = shape.get_squares()
        for square in squares:
            self.points += POINTS_FOR_SQUARE
        self.points += add_points_for_speed(self.speed)

    def add_points_for_row(self) -> None:
        self.points += POINTS_FOR_ROW

    def add_points_for_row_bonus(self, row_number: int) -> None:
        self.points += add_points_for_row_numbers(row_number)

    def get_name(self) -> str:
        return self.name

    def get_points(self) -> int:
        return self.points
