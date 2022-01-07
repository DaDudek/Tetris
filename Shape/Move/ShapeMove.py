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

def move_up(shape):
    shape.next_rotation()
