from Shape.ShapeQueue import ShapeQueue
from color.ColorService import get_white, get_black
from db.history_record.HistoryRecordRepository import get_top_ten
from drawer.Drawer import draw_board
from events.MainLoopEventHandler import *
from Speed.Speed import Speed
from model.Board import Board
from score.Score import Score
from gameSettings.SizeConstants import *
from gameSettings.FontConstants import *
from gameSettings.BoardCoordinateConstants import *

pygame.init()

pygame.display.set_caption('Tetris')
window_surface = pygame.display.set_mode((GAME_SCREEN_WIGHT, GAME_SCREEN_HIGHT))

background = pygame.Surface((GAME_SCREEN_WIGHT, GAME_SCREEN_HIGHT))
background.fill(get_white().get_color())


def init_screen_loop():
    run = True
    player_name_font = pygame.font.SysFont(FONT_NAME, INIT_SCREEN_PLAYER_NAME_FONT_SIZE)
    game_message_font = pygame.font.SysFont(FONT_NAME, INIT_SCREEN_GAME_MESSAGE_FONT_SIZE)
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

            player_text_surf = player_name_font.render(text, True, get_black().get_color())
            message_text_surf = game_message_font.render("PASS THE NAME AND CLICK ENTER", True, get_black().get_color())

            window_surface.blit(player_text_surf, player_text_surf.get_rect(center=window_surface.get_rect().center))
            window_surface.blit(message_text_surf, (INIT_SCREEN_GAME_MESSAGE_X_COORDINATE,
                                                    INIT_SCREEN_GAME_MESSAGE_Y_COORDINATE))
            pygame.display.flip()
    return text


def main_game_loop(player_name):
    next_message_font = pygame.font.SysFont(FONT_NAME, MAIN_LOOP_NEXT_FONT_SIZE)
    next_message_surface = next_message_font.render("Next", True,  get_black().get_color())

    is_running = True
    queue = ShapeQueue()

    score_font = pygame.font.SysFont(FONT_NAME, MAIN_LOOP_SCORE_FONT_SIZE)

    speed = Speed()
    score = Score(player_name, speed)

    pygame.time.set_timer(FALLING_EVENT, speed.speed_falling)
    pygame.time.set_timer(SPEED_UP_EVENT, speed.falling_speed_up_interval)

    board = Board(queue, score, speed)
    while is_running:
        shape = queue.get_current()
        is_running = handle_events(shape, board)
        window_surface.blit(background, (0, 0))
        window_surface.blit(next_message_surface, (MAIN_LOOP_NEXT_MESSAGE_X_COORDINATE,
                                                   MAIN_LOOP_NEXT_MESSAGE_Y_COORDINATE))

        score_text_surface = score_font.render("Score: " + str(board.get_score().get_points()),
                                               True, get_black().get_color())
        window_surface.blit(score_text_surface, (MAIN_LOOP_SCORE_MESSAGE_X_COORDINATE,
                                                 MAIN_LOOP_SCORE_MESSAGE_Y_COORDINATE))
        background.fill(get_white().get_color())
        draw_board(board, background, get_top_ten())
        pygame.display.flip()
    return board.get_score().get_points()

def game_over_loop(score):
    run = True
    score_font = pygame.font.SysFont(FONT_NAME, GAME_OVER_SCREEN_SCORE_FONT_SIZE)
    game_message_font = pygame.font.SysFont(FONT_NAME, GAME_OVER_MESSAGE_FONT_SIZE)
    text = ""
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                run = False
        window_surface.fill(get_white().get_color())
        background.fill(get_white().get_color())

        message_text_surf = game_message_font.render("GAME OVER, PRESS ANY BUTTON TO LEAVE", True, get_black().get_color())
        player_text_surf = score_font.render(f"YOUR SCORE: {score}", True, get_black().get_color())
        window_surface.blit(player_text_surf, player_text_surf.get_rect(center=window_surface.get_rect().center))

        window_surface.blit(message_text_surf, (GAME_OVER_SCREEN_MESSAGE_X_COORDINATE,
                                                GAME_OVER_SCREEN_MESSAGE_Y_COORDINATE))
        pygame.display.flip()
    return text

player_name = init_screen_loop()
score = main_game_loop(player_name)
game_over_loop(score)



