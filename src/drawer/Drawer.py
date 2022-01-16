from typing import Iterable

import pygame

from src.Shape.Move.ShadowMove import shadow_move
from src.color.ColorService import get_shadow, get_black
from src.db.history_record.HistoryRecord import HistoryRecord
from src.gameSettings.QueueCoordinateConstants import *
from src.model.Board import Board
from src.model.Point import Point
from src.model.Square import Square


def draw_board(board: Board,
               surface: pygame.Surface,
               history: Iterable[HistoryRecord]) -> None:
    draw_shadow(board, surface)

    draw_background(surface)

    draw_stacked_shapes(board, surface)

    draw_current_shape(board, surface)

    draw_queue(board, surface)

    draw_top_ten(history, surface)


def draw_stacked_shapes(board: Board, surface: pygame.Surface) -> None:
    draw_squares(board.get_squares(), surface)


def draw_current_shape(board: Board, surface: pygame.Surface) -> None:
    current_shape = board.get_queue().get_current()
    draw_squares(current_shape.get_squares(), surface)


def draw_square(square: Square, surface: pygame.Surface) -> None:
    pygame.draw.rect(surface,
                     square.get_color(),
                     pygame.Rect(square.getX(),
                                 square.getY(),
                                 SQUARE_SIZE,
                                 SQUARE_SIZE))


def draw_squares(squares: Iterable[Square], surface: pygame.Surface) -> None:
    for square in squares:
        draw_square(square, surface)


def draw_background(surface: pygame.Surface) -> None:
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_SQUARES_IN_ROW):
            init_x = j * SQUARE_SIZE
            init_y = i * SQUARE_SIZE
            border_coords = ((init_x, init_y),
                             (init_x + SQUARE_SIZE, init_y),
                             (init_x + SQUARE_SIZE, init_y + SQUARE_SIZE),
                             (init_x, init_y + SQUARE_SIZE))
            border_thickness = 1
            pygame.draw.lines(surface,
                              (0, 0, 0),
                              True,
                              border_coords,
                              border_thickness)


def draw_queue(board: Board,
               surface: pygame.Surface) -> None:
    for i in range(3):
        shape = board.get_queue().get_by_position(i + 1)
        previous_coordinate = shape.get_coordinate()
        shape.set_coordinate(Point(INIT_QUEUE_X,
                                   INIT_QUEUE_Y + (INIT_QUEUE_GAP * i)))
        draw_squares(shape.get_squares(), surface)
        shape.set_coordinate(previous_coordinate)


def draw_shadow(board: Board, surface: pygame.Surface):
    current_shape = board.get_queue().get_current()
    squares = board.get_all_squares_to_check()
    shadow_shape = shadow_move(current_shape, squares)
    shadow_squares = shadow_shape.get_squares()
    for square in shadow_squares:
        square.set_color(get_shadow().get_color())
    draw_squares(shadow_squares, surface)


def draw_top_ten(history: Iterable[HistoryRecord], surface: pygame.Surface):
    myfont = pygame.font.SysFont('verdana', 20)
    counter = 0
    for record in history:
        index = counter+1
        text = f"{index}. {record.get_player_name()} {record.get_points()}"
        score_text_surface = myfont.render(text,
                                           True,
                                           get_black().get_color())
        surface.blit(score_text_surface, (30 * 11, 400 + (30 * counter)))
        counter += 1
