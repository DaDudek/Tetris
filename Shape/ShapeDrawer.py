import pygame
from gameSettings.SizeConstants import *

def draw_board(board, surface):
    for square in board.get_squares():
        draw_square(square, surface)
    current_shape = board.get_queue().get_current()
    for square in current_shape.get_squares():
        draw_square(square, surface)

def draw_square(square, surface):
    pygame.draw.rect(surface, square.get_color(), pygame.Rect(square.getX(),
                                                            square.getY(),
                                                                 INIT_SQUARE_SIZE, INIT_SQUARE_SIZE))