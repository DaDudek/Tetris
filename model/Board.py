from gameSettings.SizeConstants import *
from model.Point import Point
from model.Square import Square


class Board:
    def __init__(self, queue):
        self.stacked_squares = []  # list of squares
        self.queue = queue

    def get_queue(self):
        return self.queue

    def get_squares(self):
        return self.stacked_squares


    def get_invisible_squares(self):
    # this method add some invisible squares to easier detect colision with wall/floor
        squares = []
        for i in range(NUMBER_OF_SQUARES_IN_ROW):
            squares.append(Square(Point(i * INIT_SQUARE_SIZE,
                                 INIT_HIGHT),
                                  None))
        return squares

    def add_shape(self, shape):
        for square in shape.get_squares():
            self.stacked_squares.append(square)

    # TODO add detection of walls

