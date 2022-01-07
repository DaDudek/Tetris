import sys

import pygame.event
import Shape.Move.CollisionDetector as CollisionDetector

from Shape.Move.ShapeMove import move_down, move_left, move_right, move_up

FALLING_EVENT = pygame.USEREVENT + 1


def handle_events(shape, queue):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == FALLING_EVENT:
            handle_falling(shape, queue)
        if event.type == pygame.KEYDOWN:
            handle_keyboard_press(event, shape, queue)


def handle_keyboard_press(event, shape, queue):
    if event.key == pygame.K_LEFT:
        move_left(shape)
    if event.key == pygame.K_RIGHT:
        move_right(shape)
    if event.key == pygame.K_DOWN:
        handle_falling(shape, queue)
    if event.key == pygame.K_UP:
        move_up(shape)


def handle_falling(shape, queue):
    move_down(shape)
    if CollisionDetector.check_for_vertical_collision(shape):
        queue.remove_current()
        queue.add_random_to_queue()
