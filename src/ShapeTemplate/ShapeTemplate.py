from typing import List

from src.ShapeTemplate.Box import Box
from src.color.Color import Color


class ShapeTemplate:
    def __init__(self, rotations: List[Box], color: Color):
        self.rotations: List[Box] = rotations
        self.color: Color = color

    def get_rotation(self, number: int) -> Box:
        """
        this function return box object that represent any shape.
        Every shape can be rotated in 4 ways in accordance with the Super rotation system
        from official Tetris Guideline.
        :param number:
        :return:
        """
        return self.rotations[number]
