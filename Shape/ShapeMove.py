from gameSettings.SizeConstants import *
from model.Point import Point


def move_down(shape):
    shape.set_coordinate(Point(shape.get_coordinate().getX(),
                               shape.get_coordinate().getY() + INIT_SQUARE_SIZE))
