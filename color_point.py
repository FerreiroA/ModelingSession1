from point import Point  # point is the file, Point is the class
import random

class ColorPoint(Point):
    """
    ColorPoint extends the Point class by adding a color attribute.
    """

    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with x and y coordinates and a color.

        :param x: x-coordinate (int or float)
        :param y: y-coordinate (int or float)
        :param color: color of the point (str)
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Return a string representation of the color point.

        :return: A string in the format "<x,y>(color)"
        """
        return f"<{self.x},{self.y}>({self.color})"


if __name__ == '__main__':
    """
    Main execution block:
    - Creates a list of random ColorPoint instances.
    - Prints them before and after sorting.
    """
    color_points = []
    colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
    for _ in range(5):
        p = ColorPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(colors))
        color_points.append(p)

    print("random color points:")
    print(color_points)
    color_points.sort()
    print("color points in order:")
    print(color_points)