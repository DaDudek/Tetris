class Board():
    def __init__(self, queue):
        self.stacked_squares = []  # list of squares
        self.queue = queue

    def get_queue(self):
        return self.queue

