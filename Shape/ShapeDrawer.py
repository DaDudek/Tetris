import pygame
from gameSettings.SizeConstants import *


def draw_shape(shape, surface):
    row_number = 0
    for row in shape.get_actual_rotation().rows:
        field_number = 0
        for field in row.fields:
            if field.isFill:
                pygame.draw.rect(surface, shape.get_color(), pygame.Rect(count_X_coordinate(shape, field_number),
                                                                         count_Y_coordinate(shape, row_number),
                                                                         INIT_SQUARE_SIZE, INIT_SQUARE_SIZE))
            field_number += 1
        row_number += 1


def count_X_coordinate(shape, field_number):
    return shape.get_coordinate().getX() + (INIT_SQUARE_SIZE * field_number)

def count_Y_coordinate(shape, row_number):
    return shape.get_coordinate().getY() + (INIT_SQUARE_SIZE * row_number)