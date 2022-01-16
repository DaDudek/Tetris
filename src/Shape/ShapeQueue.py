from typing import List

from src.Shape.Shape import Shape
from src.ShapeTemplate.ShapeTemplateConstructor.ShapeTemplateConstructor \
    import construct_by_id
import random


class ShapeQueue:
    def __init__(self):
        self.queue: List[Shape] = []
        self.last_index = 0
        for i in range(4):
            self.add_random_to_queue()

    def get_current(self) -> Shape:
        return self.get_by_position(0)

    def add_to_queue(self, shape: Shape) -> None:
        self.queue.append(shape)

    def add_random_to_queue(self) -> None:
        """
        this function adding random shape to queue
        - its make game more unpredictable
        new shape must be other than previous one.
        :return:
        """
        self.choose_different_then_previous()
        random_template = construct_by_id(self.last_index)
        self.add_to_queue(Shape(random_template))

    def remove_current(self) -> None:
        self.queue.pop(0)

    def choose_different_then_previous(self) -> None:
        possible_indexes = [x for x in range(7)]
        possible_indexes.remove(self.last_index)
        random_id = random.choice(possible_indexes)
        possible_indexes.append(self.last_index)
        possible_indexes.remove(random_id)
        self.last_index = random_id

    def get_by_position(self, position) -> Shape:
        """
        return element from queue that's stay on given position
        :param position:
        :return:
        """
        return self.queue[position]
