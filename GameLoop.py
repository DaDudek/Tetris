import pygame
import time

from Shape.Shape import Shape
from ShapeTemplate.ShapeTemplateConstructor import ShapeTemplateConstructor
from Shape.ShapeDrawer import draw_shape
from Shape.ShapeMove import *

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((30*10, 30*24))

background = pygame.Surface((30*10, 30*24))
background.fill(pygame.Color('#000000'))

is_running = True
shape = Shape(ShapeTemplateConstructor.LShapeConstructor.construct())
while is_running:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             is_running = False

     window_surface.blit(background, (0, 0))
     #shape = Shape(ShapeTemplateConstructor.SquareShapeConstructor.construct())
     #shape = Shape(ShapeTemplateConstructor.LongShapeConstructor.construct())
     background.fill(pygame.Color('#000000'))
     draw_shape(shape, background)
     move_down(shape)
     time.sleep(1)
     pygame.display.flip()

     #pygame.display.update()