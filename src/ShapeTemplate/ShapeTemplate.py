from typing import List

from src.ShapeTemplate.Box import Box
from src.color.Color import Color


class ShapeTemplate:
    def __init__(self, rotations: List[Box], color: Color):
        self.rotations: List[Box] = rotations
        self.color: Color = color

    def get_rotation(self, number: int) -> Box:
        return self.rotations[number]
