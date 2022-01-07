from gameSettings.SizeConstants import *


def checkForRemove(board):
    actualRow = board.get_squares()[0].getY()
    counter = 0
    possible_needed_to_be_removed = []
    actually_needed_to_be_removed = []
    for square in board.get_squares():
        possible_needed_to_be_removed.append(square)
        if square.getY() == actualRow:
            counter += 1
        else:
            actualRow = square.getY()
            counter = 1
            possible_needed_to_be_removed = [square]
        if counter == NUMBER_OF_SQUARES_IN_ROW:
            actually_needed_to_be_removed.extend(possible_needed_to_be_removed)
            possible_needed_to_be_removed = []
    board.remove_all_from_list(actually_needed_to_be_removed)
    print()


