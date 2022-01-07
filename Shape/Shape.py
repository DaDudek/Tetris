from model.Point import Point
from gameSettings.SizeConstants import *
from model.Square import Square


class Shape:
    def __init__(self, shapeTemplate):
        self.upper_left_square = Point(INIT_WIGHT/2, 0)
        self.actualRotation = 0
        self.shapeTemplate = shapeTemplate  # shape template

    def get_coordinate(self):
        return self.upper_left_square

    def get_actual_rotation(self):
        return self.shapeTemplate.get_rotation(self.actualRotation)

    def next_rotation(self):
        self.actualRotation = (self.actualRotation + 1) % 4

    def get_color(self):
        return self.shapeTemplate.color.get_color()

    def set_coordinate(self, coordinate):
        self.upper_left_square = coordinate

    def get_squares(self):
        squares = [] # list of squares
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

    def count_X_coordinate(self, field_number):
        return self.get_coordinate().getX() + (INIT_SQUARE_SIZE * field_number)

    def count_Y_coordinate(self, row_number):
        return self.get_coordinate().getY() + (INIT_SQUARE_SIZE * row_number)



