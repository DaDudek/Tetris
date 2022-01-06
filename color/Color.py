
class Color:
    def __init__(self, red, green, blue):
        self.red = red  # int
        self.green = green  # int
        self.blue = blue  # int

    def get_red_part(self):
        return self.red

    def get_blue_part(self):
        return self.blue

    def get_green_part(self):
        return self.green


COLOR_NAMES = ["RED",
               "GREEN",
               "BLUE",
               "MARITIME",
               "ORANGE",
               "YELLOW",
               "PURPLE"]

