from gameSettings.SizeConstants import *


def check_for_vertical_collision(shape, squares):
    for square in shape.get_squares():
        for stacked_square in squares:
            if square.getY() >= stacked_square.getY() and square.getX() == stacked_square.getX():
                return True
    return False


def check_for_horizontal_collision(shape):
    for square in shape.get_squares():
        if square.getX() >= INIT_WIGHT or square.getX <= 0:
            return True
    return False
