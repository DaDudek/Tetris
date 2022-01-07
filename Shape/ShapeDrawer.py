import pygame
from gameSettings.SizeConstants import *
from model.Point import Point
from model.Square import Square


def draw_board(board, surface):
    draw_backgroiund(surface)
    for square in board.get_squares():
        draw_square(square, surface)
    current_shape = board.get_queue().get_current()
    for square in current_shape.get_squares():
        draw_square(square, surface)

def draw_square(square, surface):
    pygame.draw.rect(surface, square.get_color(), pygame.Rect(square.getX(),
                                                            square.getY(),
                                                                 INIT_SQUARE_SIZE, INIT_SQUARE_SIZE))

def draw_backgroiund(surface):
    for i in range(NUMEBR_OF_ROWS):
        for j in range(NUMBER_OF_SQUARES_IN_ROW):
            init_x = j * INIT_SQUARE_SIZE
            init_y = i * INIT_SQUARE_SIZE
            border_coords = ((init_x, init_y),
                             (init_x + INIT_SQUARE_SIZE, init_y),
                             (init_x + INIT_SQUARE_SIZE, init_y + INIT_SQUARE_SIZE),
                             (init_x, init_y + INIT_SQUARE_SIZE))
            border_thickness = 1
            pygame.draw.lines(surface, (0,0,0), True, (border_coords), border_thickness)