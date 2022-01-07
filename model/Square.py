class Square:
    def __init__(self, point, color):
        self.point = point
        self.color = color

    def getX(self):
        return self.point.getX()

    def getY(self):
        return self.point.getY()

    def get_color(self):
        return self.color