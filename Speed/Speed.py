from gameSettings.SizeConstants import *


class Speed:
    def __init__(self):
        self.speed_falling = SPEED_FALLING
        self.speed_falling_increase = SPEED_FALLING_INCREASE
        self.falling_speed_up_interval = SPEED_FALLING_SPEED_UP_INTERVAL

    def get_current_speed(self):
        return self.speed_falling

    def get_interval(self):
        return self.falling_speed_up_interval

    def speed_up(self):
        self.speed_falling -= self.speed_falling_increase
        if self.speed_falling < SPEED_FALLING_MAX_SPEED:
            self.speed_falling = SPEED_FALLING_MAX_SPEED
