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
        """
        this function return information about how often
        game speed should be increased
        :return: milliseconds information
        """
        return self.falling_speed_up_interval

    def get_number_of_increases(self) -> int:
        """
        information about how many times game speed was increased
        this information it's currently used to count bonus points
        :return:
        """
        return self.numbers_of_increase

    def speed_up(self) -> None:
        """
        this function increase game speed
        to maximal game speed (to avoid unplayable speed)
        :return:
        """
        self.speed_falling -= self.speed_falling_increase
        if self.speed_falling < SPEED_FALLING_MAX_SPEED:
            self.speed_falling = SPEED_FALLING_MAX_SPEED
        else:
            self.numbers_of_increase += 1
