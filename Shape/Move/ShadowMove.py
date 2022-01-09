from typing import Iterable

import Shape.Move.CollisionDetector as CollisionDetector
from Shape.Move.ShapeMove import move_down, move_up
from Shape.Shape import Shape
from model.Square import Square


def shadow_move(shape: Shape, squares: Iterable[Square]) -> Shape:
    shadow_shape = Shape(shape.get_template(), shape.get_rotation_number(), shape.get_coordinate())
    while not CollisionDetector.check_for_collision(shadow_shape, squares):
        move_down(shadow_shape)
    move_up(shadow_shape)
    return shadow_shape
