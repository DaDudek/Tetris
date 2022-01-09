from typing import List

from src.ShapeTemplate.Row import Row


class Box:
    def __init__(self, rows: List[Row]):
        self.rows = rows
