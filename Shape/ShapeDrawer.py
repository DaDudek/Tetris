import pygame
from gameSettings.SizeConstants import *


def draw_shape(shape, surface):
    for point in shape.get_points():
        pygame.draw.rect(surface, shape.get_color(), pygame.Rect(point.getX(),
                                                                 point.getY(),
                                                                 INIT_SQUARE_SIZE, INIT_SQUARE_SIZE))