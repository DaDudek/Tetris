from src.Speed.Speed import Speed
from src.gameSettings.BonusPointsConstants import *


def add_points_for_speed(speed: Speed) -> int:
    return speed.get_number_of_increases() * SPEED_FALLING_BONUS


def add_points_for_row_numbers(number_of_destroyed_rows_in_move: int) -> int:
    return number_of_destroyed_rows_in_move * BONUS_FOR_ROW_IN_ONE_MOVE
