from ShapeTemplate.ShapeTemplateConstructor import LongShapeConstructor, ReverseLShapeConstructor, LShapeConstructor, \
    SquareShapeConstructor, ReverseZShapeConstructor, ZShapeConstructor


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