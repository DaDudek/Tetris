from typing import Tuple

from color.Color import Color
from model.Point import Point


class Square:
    def __init__(self, point: Point, color: Tuple[int, int, int]):
        self.point = point
        self.color = color

    def getX(self) -> int:
        return self.point.getX()

    def getY(self) -> int:
        return self.point.getY()

    def setY(self, Y) -> None:
        self.point.setY(Y)

    def get_color(self) -> Tuple[int, int, int]:
        return self.color

    def set_color(self, color: Tuple[int, int, int]) -> None:
        self.color = color
