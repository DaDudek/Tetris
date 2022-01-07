from Shape.Shape import Shape
from ShapeTemplate.ShapeTemplateConstructor.ShapeTemplateConstructor import construct_by_id
import random

class ShapeQueue:
    def __init__(self):
        self.queue = []  #shape queue
        for i in range(4):
            self.add_random_to_queue()

    def get_current(self):
        return self.queue[0]

    def add_to_queue(self, shape):
        self.queue.append(shape)

    def add_random_to_queue(self):
        random_template = construct_by_id(random.randint(0, 6))
        self.add_to_queue(Shape(random_template))

    def remove_current(self):
        self.queue.pop(0)

