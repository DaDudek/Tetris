import sys

import pygame.event
import src.Shape.Move.CollisionDetector as CollisionDetector

from src.Shape.Move.ShapeMove import move_down, move_left, \
    move_right, rotate, move_up
from src.Shape.Shape import Shape
from src.db.history_record.HistoryRecord import HistoryRecord
from src.db.history_record.HistoryRecordRepository import save
from src.model.Board import Board

FALLING_EVENT = pygame.USEREVENT + 1
GAME_OVER_EVENT = pygame.USEREVENT + 2
SPEED_UP_EVENT = pygame.USEREVENT + 3


def handle_events(shape: Shape, board: Board) -> bool:
    for event in pygame.event.get():
        if event.type == SPEED_UP_EVENT:
            speed = board.get_speed()
            speed.speed_up()
            pygame.time.set_timer(FALLING_EVENT, speed.get_current_speed())
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == FALLING_EVENT:
            handle_falling(shape, board)
        if event.type == pygame.KEYDOWN:
            handle_keyboard_press(event, shape, board)
        if event.type == GAME_OVER_EVENT:
            points = board.get_score().get_points()
            name = board.get_score().get_name()
            history_record = HistoryRecord(points=points,
                                           player_name=name)
            save(history_record)
            return False
    return True


def handle_keyboard_press(event: pygame.event.Event,
                          shape: Shape,
                          board: Board) -> None:
    all_squares = board.get_all_squares_to_check()
    if event.key == pygame.K_LEFT:
        move_left(shape)
        if CollisionDetector.check_for_collision(shape,
                                                 all_squares):
            move_right(shape)
    if event.key == pygame.K_RIGHT:
        move_right(shape)
        if CollisionDetector.check_for_collision(shape,
                                                 all_squares):
            move_left(shape)
    if event.key == pygame.K_DOWN:
        handle_falling(shape, board)
    if event.key == pygame.K_UP:
        rotate(shape)
        if CollisionDetector.check_for_collision(shape,
                                                 all_squares):
            shape.previous_rotation()


def handle_falling(shape: Shape, board: Board) -> None:
    move_down(shape)
    queue = board.get_queue()
    all_squares = board.get_all_squares_to_check()
    if CollisionDetector.check_for_collision(shape,
                                             all_squares):
        move_up(shape)
        board.add_shape(shape)
        board.add_point_for_shape(shape)
        queue.remove_current()
        queue.add_random_to_queue()
        check_for_game_over(board)


def check_for_game_over(board: Board) -> None:
    queue = board.get_queue()
    current = queue.get_current()
    squares = board.get_all_squares_to_check()
    game_over = CollisionDetector.check_for_collision(current,
                                                      squares)
    if game_over:
        event = pygame.event.Event(GAME_OVER_EVENT)
        pygame.event.post(event)
