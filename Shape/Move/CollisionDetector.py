from gameSettings.SizeConstants import *


def check_for_vertical_collision(shape):
    for square in shape.get_squares():
        if square.getY() >= INIT_HIGHT:
            return True
    return False


def check_for_horizontal_collision(shape):
    for square in shape.get_squares():
        if square.getX() >= INIT_WIGHT or square.getX <= 0:
            return True
    return False
