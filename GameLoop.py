from Shape.ShapeQueue import ShapeQueue
from color.ColorService import get_white, get_black
from drawer.Drawer import draw_board
from events.MainLoopEventHandler import *
from Speed.Speed import Speed
from model.Board import Board
from score.Score import Score
from gameSettings.SizeConstants import *

pygame.init()

pygame.display.set_caption('Tetris')
window_surface = pygame.display.set_mode((INIT_SQUARE_SIZE * INIT_GAME_WIGHT, INIT_HIGHT))

background = pygame.Surface((INIT_SQUARE_SIZE * INIT_GAME_WIGHT, INIT_HIGHT))
background.fill(get_white().get_color())


def init_screen_loop():
    run = True
    font = pygame.font.SysFont("Comic Sans MS", 60)
    font2 = pygame.font.SysFont("Comic Sans MS", 30)
    text = ""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

            window_surface.fill(get_white().get_color())
            background.fill(get_white().get_color())

            player_text_surf = font.render(text, True, get_black().get_color())
            message_text_surf = font2.render("PASS THE NAME AND CLICK ENTER", True, get_black().get_color())

            window_surface.blit(player_text_surf, player_text_surf.get_rect(center=window_surface.get_rect().center))
            window_surface.blit(message_text_surf, (80, 300))
            pygame.display.flip()
    return text


def main_game_loop(player_name):
    myfont = pygame.font.SysFont("Comic Sans MS", 60)
    textsurface = myfont.render("Next", False, (0, 0, 0))

    is_running = True
    queue = ShapeQueue()

    score_font = pygame.font.SysFont("Comic Sans MS", 30)

    speed = Speed()
    score = Score(player_name, speed)

    pygame.time.set_timer(FALLING_EVENT, speed.speed_falling)
    pygame.time.set_timer(SPEED_UP_EVENT, speed.falling_speed_up_interval)

    board = Board(queue, score, speed)
    while is_running:
        shape = queue.get_current()
        handle_events(shape, board)
        window_surface.blit(background, (0, 0))
        window_surface.blit(textsurface, (30 * 12, 0))

        score_text_surface = score_font.render("Score: " + str(board.get_score().get_points()),
                                               False, get_black().get_color())
        window_surface.blit(score_text_surface, (30 * 11, 400))
        background.fill(get_white().get_color())
        draw_board(board, background)
        pygame.display.flip()


player_name = init_screen_loop()
main_game_loop(player_name)
