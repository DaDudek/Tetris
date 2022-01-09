from Shape.ShapeQueue import ShapeQueue
from color.ColorService import get_white, get_black
from db.history_record.HistoryRecordRepository import get_top_ten
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
    font = pygame.font.SysFont("verdana", 45)
    font2 = pygame.font.SysFont("verdana", 20)
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
    myfont = pygame.font.SysFont("verdana", 60)
    textsurface = myfont.render("Next", True, (0, 0, 0))

    is_running = True
    queue = ShapeQueue()

    score_font = pygame.font.SysFont("verdana", 25)

    speed = Speed()
    score = Score(player_name, speed)

    pygame.time.set_timer(FALLING_EVENT, speed.speed_falling)
    pygame.time.set_timer(SPEED_UP_EVENT, speed.falling_speed_up_interval)

    board = Board(queue, score, speed)
    while is_running:
        shape = queue.get_current()
        is_running = handle_events(shape, board)
        window_surface.blit(background, (0, 0))
        window_surface.blit(textsurface, (30 * 11.5, 0))

        score_text_surface = score_font.render("Score: " + str(board.get_score().get_points()),
                                               True, get_black().get_color())
        window_surface.blit(score_text_surface, (30 * 11, 360))
        background.fill(get_white().get_color())
        draw_board(board, background, get_top_ten())
        pygame.display.flip()
    return board.get_score().get_points()

def game_over_loop(score):
    run = True
    font = pygame.font.SysFont("verdana", 45)
    font2 = pygame.font.SysFont("verdana", 20)
    text = ""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                run = False
        window_surface.fill(get_white().get_color())
        background.fill(get_white().get_color())

        message_text_surf = font2.render("GAME OVER, PRESS ANY BUTTON TO LEAVE", True, get_black().get_color())
        player_text_surf = font.render(f"YOUR SCORE: {score}", True, get_black().get_color())
        window_surface.blit(player_text_surf, player_text_surf.get_rect(center=window_surface.get_rect().center))

        window_surface.blit(message_text_surf, (35, 300))
        pygame.display.flip()
    return text

player_name = init_screen_loop()
score = main_game_loop(player_name)
game_over_loop(score)



