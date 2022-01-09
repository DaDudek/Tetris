from src.gameSettings.SpeedFallingConstants import *


class Speed:
    def __init__(self):
        self.speed_falling: int = SPEED_FALLING
        self.speed_falling_increase: int = SPEED_FALLING_INCREASE
        self.falling_speed_up_interval: int = SPEED_FALLING_SPEED_UP_INTERVAL
        self.numbers_of_increase: int = 0

    def get_current_speed(self) -> int:
        return self.speed_falling

    def get_interval(self) -> int:
        return self.falling_speed_up_interval

    def get_number_of_increases(self) -> int:
        return self.numbers_of_increase

    def speed_up(self) -> None:
        self.speed_falling -= self.speed_falling_increase
        if self.speed_falling < SPEED_FALLING_MAX_SPEED:
            self.speed_falling = SPEED_FALLING_MAX_SPEED
        else:
            self.numbers_of_increase += 1
