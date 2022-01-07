def check_for_collision(shape, squares):
    for square in shape.get_squares():
        for stacked_square in squares:
            if square.getY() == stacked_square.getY() and square.getX() == stacked_square.getX():
                return True
    return False
