from gameSettings.SizeConstants import *
from model.Point import Point


def move_down(shape):
    shape.set_coordinate(Point(shape.get_coordinate().getX(),
                               shape.get_coordinate().getY() + INIT_SQUARE_SIZE))

def move_left(shape):
    shape.set_coordinate(Point(shape.get_coordinate().getX()-INIT_SQUARE_SIZE,
                               shape.get_coordinate().getY()))

def move_right(shape):
    shape.set_coordinate(Point(shape.get_coordinate().getX()+INIT_SQUARE_SIZE,
                               shape.get_coordinate().getY()))

def rotate(shape):
    shape.next_rotation()

def move_up(shape):
    shape.set_coordinate(Point(shape.get_coordinate().getX(),
                               shape.get_coordinate().getY() - INIT_SQUARE_SIZE))

def move_square_down(square):
    square.setY(square.getY() + INIT_SQUARE_SIZE)


def move_board_part_down(board, square_to_move):
    for square in board.get_squares():
        if square in square_to_move:
            move_square_down(square)

