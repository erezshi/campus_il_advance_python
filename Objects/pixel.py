class Pixel:
    def __init__(self, x=0, y=0, red=0, blue=0, green=0):
        self._x = x
        self._y = y
        self._red = red
        self._blue = blue
        self._green = green

    def set_cords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = int(sum([self._red, self._blue, self._green]) / 3)
        self._red = average
        self._blue = average
        self._green = average

    def print_pixel_info(self):
        var = f"X: {self._x} Y: {self._y} Color: {(self._red, self._green, self._blue)}"
        non_zero = ""
        if self._red == 0 and self._blue == 0:
            non_zero = "Green"
        elif self._red == 0 and self._green == 0:
            non_zero = "Blue"
        else:
            non_zero = "Red"
        print(var + non_zero)
        
def mainpixel():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

mainpixel()

