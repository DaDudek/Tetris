from gameSettings.SizeConstants import *


def check_for_vertical_collision(shape):
    for point in shape.get_points():
        if point.getY() >= INIT_HIGHT:
            return True
    return False


def check_for_horizontal_collision(shape):
    for point in shape.get_points():
        if point.getX() >= INIT_WIGHT or point.getX <= 0:
            return True
    return False
