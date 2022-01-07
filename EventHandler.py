import sys

import pygame.event
import Shape.Move.CollisionDetector as CollisionDetector

from Shape.Move.ShapeMove import move_down, move_left, move_right, rotate, move_up

FALLING_EVENT = pygame.USEREVENT + 1


def handle_events(shape, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == FALLING_EVENT:
            handle_falling(shape, board)
        if event.type == pygame.KEYDOWN:
            handle_keyboard_press(event, shape, board)


def handle_keyboard_press(event, shape, board):
    if event.key == pygame.K_LEFT:
        move_left(shape)
    if event.key == pygame.K_RIGHT:
        move_right(shape)
    if event.key == pygame.K_DOWN:
        handle_falling(shape, board)
    if event.key == pygame.K_UP:
        rotate(shape)


def handle_falling(shape, board):
    move_down(shape)
    queue = board.get_queue()
    stacked_squares = board.get_invisible_squares()
    stacked_squares.extend(board.get_squares())
    if CollisionDetector.check_for_vertical_collision(shape, stacked_squares):
        move_up(shape)
        board.add_shape(shape)
        queue.remove_current()
        queue.add_random_to_queue()
