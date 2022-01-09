from typing import Iterable

from Shape.Shape import Shape
from gameSettings.SizeConstants import *
from model.Point import Point
from model.Square import Square


def move_down(shape: Shape) -> None:
    shape.set_coordinate(Point(shape.get_coordinate().getX(),
                               shape.get_coordinate().getY() + SQUARE_SIZE))


def move_left(shape: Shape) -> None:
    shape.set_coordinate(Point(shape.get_coordinate().getX() - SQUARE_SIZE,
                               shape.get_coordinate().getY()))


def move_right(shape: Shape) -> None:
    shape.set_coordinate(Point(shape.get_coordinate().getX() + SQUARE_SIZE,
                               shape.get_coordinate().getY()))


def rotate(shape: Shape) -> None:
    shape.next_rotation()


def move_up(shape: Shape) -> None:
    shape.set_coordinate(Point(shape.get_coordinate().getX(),
                               shape.get_coordinate().getY() - SQUARE_SIZE))


def move_square_down(square: Square) -> None:
    square.setY(square.getY() + SQUARE_SIZE)


def move_board_part_down(board, squares_to_move: Iterable[Square]) -> None:
    for square in board.get_squares():
        if square in squares_to_move:
            move_square_down(square)
