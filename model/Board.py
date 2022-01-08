from gameSettings.SizeConstants import *
from model.Point import Point
from model.Square import Square
import destoryRow.rowChecker



class Board:
    def __init__(self, queue, score):
        self.stacked_squares = []  # list of squares
        self.queue = queue
        self.score = score

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


    def get_invisible_squares(self):
    # this method add some invisible squares to easier detect colision with wall/floor
        squares = []
        for i in range(NUMBER_OF_SQUARES_IN_ROW):
            squares.append(Square(Point(i * INIT_SQUARE_SIZE,
                                 INIT_HIGHT),
                                  None))
        for i in range(NUMBER_OF_ROWS):
            squares.append(Square(Point(-INIT_SQUARE_SIZE,
                                        i*INIT_SQUARE_SIZE),
                                  None))
            squares.append(Square(Point(INIT_WIGHT,
                                        i * INIT_SQUARE_SIZE),
                                  None))

        return squares

    def get_all_squares_to_check(self):
        squares = self.get_invisible_squares()
        squares.extend(self.stacked_squares)
        return squares

    def add_shape(self, shape):
        for square in shape.get_squares():
            self.stacked_squares.append(square)
        self.stacked_squares = sorted(self.stacked_squares, key = lambda point: (point.getY(), point.getX()))
        destoryRow.rowChecker.checkForRemove(self)

    def remove_all_from_list(self, squares):
        for square in squares:
            if square in self.stacked_squares:
                self.stacked_squares.remove(square)
