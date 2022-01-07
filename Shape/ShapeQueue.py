from Shape.Shape import Shape
from ShapeTemplate.ShapeTemplateConstructor.ShapeTemplateConstructor import construct_by_id
import random


class ShapeQueue:
    def __init__(self):
        self.queue = []  # shape queue
        self.last_index = 0
        for i in range(4):
            self.add_random_to_queue()

    def get_current(self):
        return self.queue[0]

    def add_to_queue(self, shape):
        self.queue.append(shape)

    def add_random_to_queue(self):
        self.choose_different_then_previous()
        random_template = construct_by_id(self.last_index)
        self.add_to_queue(Shape(random_template))

    def remove_current(self):
        self.queue.pop(0)

    def choose_different_then_previous(self):
        possible_indexes = [x for x in range(7)]
        possible_indexes.remove(self.last_index)
        random_id = random.choice(possible_indexes)
        possible_indexes.append(self.last_index)
        possible_indexes.remove(random_id)
        self.last_index = random_id
