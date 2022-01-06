from model.Point import Point


class Shape():
    def __init__(self):
        self.upper_left_square = Point()
        self.actualRotation = 0
        self.shapeTemplate = None  # shape template

    def get_points(self):
        return self.points

    def set_points(self, points_list):
        self.points = points_list

    def get_actual_rotation(self):
        return self.shapeTemplate.get_rotation(self.actualRotation)

    def get_next_rotation(self):
        self.actualRotation = (self.actualRotation + 1) % 4
        return self.get_actual_rotation()



