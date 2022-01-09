from typing import Iterable

from src.Shape.Shape import Shape
from src.model.Square import Square


def check_for_collision(shape: Shape, squares: Iterable[Square]) -> bool:
    for square in shape.get_squares():
        for stacked_square in squares:
            if square.getY() == stacked_square.getY() and square.getX() == stacked_square.getX():
                return True
    return False
