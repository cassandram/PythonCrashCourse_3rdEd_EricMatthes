

class Box:
    """ a box for a cat. """
    def __init__(self, length, width, height):
        """ creates a box object for a cat to enjoy. """
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """ returns the box length. """
        return self._length

    def get_width(self):
        """ returns the box width. """
        return self._width

    def get_height(self):
        """ return box height. """
        return self._height

    def set_box_length(self, set_length):
        """ sets the box length. """
        self._length = set_length

    def set_box_width(self, set_width):
        """ sets the box width. """
        self._width = set_width

    def calculate_volume(self):
        return self._length * self._width * self._height

    def calculate_surface_area(self):
        l = self._length
        w = self._width
        h = self._height
        return 2 * ((l * w) + (l * h) + (w * h))


psl_box = Box(5, 9, 4)


if __name__ == '__main__':
    print(psl_box.calculate_surface_area())

