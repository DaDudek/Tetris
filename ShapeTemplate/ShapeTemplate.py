from typing import List

from ShapeTemplate.Box import Box
from color.Color import Color


class ShapeTemplate:
    def __init__(self, rotations: List[Box], color: Color):
        self.rotations: List[Box] = rotations
        self.color: Color = color

    def get_rotation(self, number: int) -> Box:
        return self.rotations[number]
