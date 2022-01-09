class ShapeTemplate:
    def __init__(self, rotations, color):
        self.rotations = rotations
        self.color = color

    def get_rotation(self, number):
        return self.rotations[number]
