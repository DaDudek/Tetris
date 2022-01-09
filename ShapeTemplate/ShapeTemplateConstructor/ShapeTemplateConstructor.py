from ShapeTemplate.ShapeTemplateConstructor import LongShapeConstructor, ReverseLShapeConstructor, LShapeConstructor, \
    SquareShapeConstructor, ReverseZShapeConstructor, ZShapeConstructor, TShapeConstructor


def construct_by_id(id):
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


def construct_long_shape():
    return LongShapeConstructor.construct()


def construct_l_shape():
    return LShapeConstructor.construct()


def construct_reverse_l_shape():
    return ReverseLShapeConstructor.construct()


def construct_square_shape():
    return SquareShapeConstructor.construct()


def construct_reverse_z_shape():
    return ReverseZShapeConstructor.construct()


def construct_z_shape():
    return ZShapeConstructor.construct()


def construct_t_shape():
    return TShapeConstructor.construct()
