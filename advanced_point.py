from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    """
    AdvancedPoint extends the ColorPoint class to model a 2D point with restricted color options,
    type validation, and additional utility methods.
    """

    COLORS = ["red", "green", "blue", "black", "white"]

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint with coordinates and a color. Validates inputs.

        :param x: x-coordinate (must be int or float)
        :param y: y-coordinate (must be int or float)
        :param color: color string (must be one of the allowed COLORS)
        :raises TypeError: if x or y are not numeric
        :raises ValueError: if color is not in the COLORS list
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        # super().__init__(x, y, color) # call the init method of the parent
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Get the x-coordinate of the point.
        :return: float or int
        """
        return self._x

    @property
    def y(self):
        """
        Get the y-coordinate of the point.
        :return: float or int
        """
        return self._y

    @property
    def color(self):
        """
        Get the color of the point.
        :return: str
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Set a new color for the point if it's in the allowed list.

        :param new_color: str
        :raises ValueError: if the new color is not in COLORS
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        """
        Add a new color to the class-level COLORS list.

        :param new_color: str
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Compute Euclidean distance between two AdvancedPoint instances.

        :param p1: AdvancedPoint
        :param p2: AdvancedPoint
        :return: float
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)**0.5

    @staticmethod
    def from_dictionary(dict):
        """
        Create an AdvancedPoint from a dictionary. Uses defaults if keys are missing.

        :param dict: dictionary with optional keys 'x', 'y', and 'color'
        :return: AdvancedPoint instance
        """
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x, y, color)


# Example usage
AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(1, 2, "amber")
p2.color = "blue"
p3 = AdvancedPoint(-1, -2, "blue")
print(AdvancedPoint.distance_2_points(p2, p3))
p4 = AdvancedPoint.from_dictionary({"x": 44})
print(p4)