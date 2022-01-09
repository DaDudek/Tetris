from typing import List

from Shape.Shape import Shape
from Shape.ShapeQueue import ShapeQueue
from Speed.Speed import Speed
from gameSettings.SizeConstants import *
from model.Point import Point
from model.Square import Square
from destoryRow.rowChecker import check_for_remove
from score.Score import Score


def get_invisible_squares() -> List[Square]:
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
    def __init__(self, queue: ShapeQueue, score: Score, speed: Speed):
        self.stacked_squares: List[Square] = []
        self.queue = queue
        self.score = score
        self.speed = speed

    def get_speed(self) -> Speed:
        return self.speed

    def get_score(self) -> Score:
        return self.score

    def get_queue(self) -> ShapeQueue:
        return self.queue

    def get_squares(self) -> List[Square]:
        return self.stacked_squares

    def add_point_for_shape(self, shape: Shape) -> None:
        self.score.add_point_for_shape(shape)

    def add_point_for_row(self) -> None:
        self.score.add_points_for_row()

    def get_all_squares_to_check(self) -> List[Square]:
        squares = get_invisible_squares()
        squares.extend(self.stacked_squares)
        return squares

    def add_shape(self, shape: Shape) -> None:
        for square in shape.get_squares():
            self.stacked_squares.append(square)
        self.stacked_squares = sorted(self.stacked_squares, key=lambda point: (point.getY(), point.getX()))
        check_for_remove(self)

    def remove_all_from_list(self, squares: List[Square]) -> None:
        for square in squares:
            if square in self.stacked_squares:
                self.stacked_squares.remove(square)
