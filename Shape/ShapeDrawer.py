import pygame
from gameSettings.SizeConstants import *


def draw_shape(squares, surface):
    for square in squares:
        pygame.draw.rect(surface, square.get_color(), pygame.Rect(square.getX(),
                                                                 square.getY(),
                                                                 INIT_SQUARE_SIZE, INIT_SQUARE_SIZE))