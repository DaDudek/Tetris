from src.ShapeTemplate.ShapeTemplate import ShapeTemplate
from src.ShapeTemplate.ShapeTemplateConstructor import TShapeConstructor,\
    SquareShapeConstructor, LongShapeConstructor, \
    ZShapeConstructor, ReverseLShapeConstructor,\
    LShapeConstructor, ReverseZShapeConstructor


def construct_by_id(id: int) -> ShapeTemplate:
    if id == 0:
        return construct_long_shape()
    if id == 1:
        return construct_l_shape()
    if id == 2:
        return construct_reverse_l_shape()
    if id == 3:
        return construct_square_shape()
    if id == 4:
        return construct_reverse_z_shape()
    if id == 5:
        return construct_z_shape()
    if id == 6:
        return construct_t_shape()


def construct_long_shape() -> ShapeTemplate:
    return LongShapeConstructor.construct()


def construct_l_shape() -> ShapeTemplate:
    return LShapeConstructor.construct()


def construct_reverse_l_shape() -> ShapeTemplate:
    return ReverseLShapeConstructor.construct()


def construct_square_shape() -> ShapeTemplate:
    return SquareShapeConstructor.construct()


def construct_reverse_z_shape() -> ShapeTemplate:
    return ReverseZShapeConstructor.construct()


def construct_z_shape() -> ShapeTemplate:
    return ZShapeConstructor.construct()


def construct_t_shape() -> ShapeTemplate:
    return TShapeConstructor.construct()
