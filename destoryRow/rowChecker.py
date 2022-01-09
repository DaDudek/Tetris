from gameSettings.SizeConstants import *
from Shape.Move.ShapeMove import move_board_part_down


def check_for_remove(board):
    something_was_removed = True
    number_of_removed_rows = 0
    while something_was_removed:
        something_was_removed = False
        if not board.get_squares():
            break
        actual_row = board.get_squares()[0].getY()
        counter = 0
        possible_needed_to_be_removed = []
        checked_squares = []
        for square in board.get_squares():
            possible_needed_to_be_removed.append(square)
            checked_squares.append(square)
            if square.getY() == actual_row:
                counter += 1
            else:
                actual_row = square.getY()
                counter = 1
                possible_needed_to_be_removed = [square]
            if counter == NUMBER_OF_SQUARES_IN_ROW:
                something_was_removed = True
                break
        if len(possible_needed_to_be_removed) == NUMBER_OF_SQUARES_IN_ROW:
            board.remove_all_from_list(possible_needed_to_be_removed)
            board.add_point_for_row()
            move_board_part_down(board, checked_squares)
            number_of_removed_rows += 1
    board.get_score().add_points_for_row_bonus(number_of_removed_rows)