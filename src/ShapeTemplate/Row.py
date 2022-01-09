from typing import List

from src.ShapeTemplate.Field import Field


class Row:
    def __init__(self, fields: List[Field]):
        self.fields = fields
