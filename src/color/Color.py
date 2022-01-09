from typing import Tuple


class Color:
    def __init__(self, red: int, green: int, blue: int):
        self.red: int = red
        self.green: int = green
        self.blue: int = blue

    def get_red_part(self) -> int:
        return self.red

    def get_blue_part(self) -> int:
        return self.blue

    def get_green_part(self) -> int:
        return self.green

    def get_color(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue

