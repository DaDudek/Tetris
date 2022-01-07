import sys

import pygame.event

from Shape.ShapeMove import move_down, move_left, move_right, move_up

FALLING_EVENT = pygame.USEREVENT+1

def handle_events(shape):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == FALLING_EVENT:
            move_down(shape)
        if event.type == pygame.KEYDOWN:
            handle_keyboard_press(event,shape)

def handle_keyboard_press(event, shape):
    if event.key == pygame.K_LEFT:
        move_left(shape)
    if event.key == pygame.K_RIGHT:
        move_right(shape)
    if event.key == pygame.K_DOWN:
        move_down(shape)
    if event.key == pygame.K_UP:
        move_up(shape)
