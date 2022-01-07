import pygame
import time

from Shape.Shape import Shape
from Shape.ShapeQueue import ShapeQueue
from ShapeTemplate.ShapeTemplateConstructor import ShapeTemplateConstructor
from Shape.ShapeDrawer import draw_shape
from EventHandler import *
pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((30*10, 30*24))

background = pygame.Surface((30*10, 30*24))
background.fill(pygame.Color('#000000'))

is_running = True
queue = ShapeQueue()
pygame.time.set_timer(FALLING_EVENT,  1000)
while is_running:
    shape = queue.get_current()
    handle_events(shape)
    window_surface.blit(background, (0, 0))
    background.fill(pygame.Color('#000000'))
    draw_shape(shape, background)
    pygame.display.flip()

     #pygame.display.update()