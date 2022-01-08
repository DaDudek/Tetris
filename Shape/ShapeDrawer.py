import pygame
from gameSettings.SizeConstants import *
from model.Point import Point


def draw_board(board, surface):
    draw_background(surface)
    draw_squares(board.get_squares(), surface)
    current_shape = board.get_queue().get_current()
    draw_squares(current_shape.get_squares(), surface)
    draw_queue(board, surface)

def draw_square(square, surface):
    pygame.draw.rect(surface, square.get_color(), pygame.Rect(square.getX(),
                                                            square.getY(),
                                                                 INIT_SQUARE_SIZE, INIT_SQUARE_SIZE))
def draw_squares(squares,surface):
    for square in squares:
        draw_square(square, surface)

def draw_background(surface):
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_SQUARES_IN_ROW):
            init_x = j * INIT_SQUARE_SIZE
            init_y = i * INIT_SQUARE_SIZE
            border_coords = ((init_x, init_y),
                             (init_x + INIT_SQUARE_SIZE, init_y),
                             (init_x + INIT_SQUARE_SIZE, init_y + INIT_SQUARE_SIZE),
                             (init_x, init_y + INIT_SQUARE_SIZE))
            border_thickness = 1
            pygame.draw.lines(surface, (0,0,0), True, (border_coords), border_thickness)

def draw_queue(board, surface):
    for i in range(3):
        shape = board.get_queue().get_by_position(i+1)
        previous_coordinate = shape.get_coordinate()
        shape.set_coordinate(Point(INIT_QUEUE_X, INIT_QUEUE_Y + (INIT_QUEUE_GAP * i)))
        draw_squares(shape.get_squares(), surface)
        shape.set_coordinate(previous_coordinate)
