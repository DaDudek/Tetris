from Shape.ShapeQueue import ShapeQueue
from Shape.ShapeDrawer import draw_board
from EventHandler import *
from model.Board import Board

pygame.init()

pygame.display.set_caption('Tetris')
window_surface = pygame.display.set_mode((30*17, 30*24))

background = pygame.Surface((30*17, 30*24))
background.fill((255, 255, 255))

myfont = pygame.font.SysFont("Comic Sans MS", 60)
textsurface = myfont.render("Next", False, (0, 0, 0))

is_running = True
queue = ShapeQueue()
board = Board(queue)
pygame.time.set_timer(FALLING_EVENT,  1000)
while is_running:
    shape = queue.get_current()
    handle_events(shape, board)
    window_surface.blit(background, (0, 0))
    window_surface.blit(textsurface, (30*12, 0))
    background.fill((255, 255, 255))
    draw_board(board, background)
    pygame.display.flip()

     #pygame.display.update()