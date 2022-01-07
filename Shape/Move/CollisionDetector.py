from gameSettings.SizeConstants import *


def check_for_collision(shape):
    for point in shape.get_points():
        if check_for_vertical_collision(point) or check_for_horizontal_collision(point):
            return True
    return False


def check_for_vertical_collision(point):
    return point.getY() >= INIT_HIGHT


def check_for_horizontal_collision(point):
    return point.getX() >= INIT_WIGHT or point.getX <= 0
