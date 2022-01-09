from typing import Iterable, Tuple

from ShapeTemplate.Box import Box
from ShapeTemplate.ShapeTemplate import ShapeTemplate
from model.Point import Point
from gameSettings.SizeConstants import *
from model.Square import Square


class Shape:
    def __init__(self, shapeTemplate: ShapeTemplate,
                 actualRotation: int = 0,
                 upper_left_square: Point = Point(BOARD_WIGHT / 2, 0)):
        self.upper_left_square = upper_left_square
        self.actualRotation = actualRotation
        self.shapeTemplate = shapeTemplate

    def get_coordinate(self) -> Point:
        return self.upper_left_square

    def get_template(self) -> ShapeTemplate:
        return self.shapeTemplate

    def get_actual_rotation(self) -> Box:
        return self.shapeTemplate.get_rotation(self.actualRotation)

    def get_rotation_number(self) -> int:
        return self.actualRotation

    def next_rotation(self) -> None:
        self.actualRotation = (self.actualRotation + 1) % 4

    def previous_rotation(self) -> None:
        self.actualRotation = (self.actualRotation - 1) % 4

    def get_color(self) -> Tuple[int, int, int]:
        return self.shapeTemplate.color.get_color()

    def set_coordinate(self, coordinate: Point) -> None:
        self.upper_left_square = coordinate

    def get_squares(self) -> Iterable[Square]:
        squares = []
        row_number = 0
        for row in self.get_actual_rotation().rows:
            field_number = 0
            for field in row.fields:
                if field.isFill:
                    squares.append(
                        Square(
                            Point(self.count_X_coordinate(field_number),
                                  self.count_Y_coordinate(row_number)),
                            self.get_color()))
                field_number += 1
            row_number += 1
        return squares

    def count_X_coordinate(self, field_number: int) -> int:
        return self.get_coordinate().getX() + (SQUARE_SIZE * field_number)

    def count_Y_coordinate(self, row_number: int) -> int:
        return self.get_coordinate().getY() + (SQUARE_SIZE * row_number)
