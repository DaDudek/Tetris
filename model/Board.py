from gameSettings.SizeConstants import *
from model.Point import Point
from model.Square import Square
import destoryRow.rowChecker


def get_invisible_squares():
    # this method add some invisible squares to easier detect collision with wall/floor
    squares = []
    for i in range(NUMBER_OF_SQUARES_IN_ROW):
        squares.append(Square(Point(i * SQUARE_SIZE,
                                    GAME_SCREEN_HIGHT),
                              None))
    for i in range(NUMBER_OF_ROWS):
        squares.append(Square(Point(-SQUARE_SIZE,
                                    i * SQUARE_SIZE),
                              None))
        squares.append(Square(Point(BOARD_WIGHT,
                                    i * SQUARE_SIZE),
                              None))

    return squares


class Board:
    def __init__(self, queue, score, speed):
        self.stacked_squares = []  # list of squares
        self.queue = queue
        self.score = score
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_score(self):
        return self.score

    def get_queue(self):
        return self.queue

    def get_squares(self):
        return self.stacked_squares

    def add_point_for_shape(self, shape):
        self.score.add_point_for_shape(shape)

    def add_point_for_row(self):
        self.score.add_points_for_row()

    def get_all_squares_to_check(self):
        squares = get_invisible_squares()
        squares.extend(self.stacked_squares)
        return squares

    def add_shape(self, shape):
        for square in shape.get_squares():
            self.stacked_squares.append(square)
        self.stacked_squares = sorted(self.stacked_squares, key=lambda point: (point.getY(), point.getX()))
        destoryRow.rowChecker.check_for_remove(self)

    def remove_all_from_list(self, squares):
        for square in squares:
            if square in self.stacked_squares:
                self.stacked_squares.remove(square)
