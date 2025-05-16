import random
from ftplib import parse227


class Point:
    """
    Class modeling a real-life 2D point with basic geometric operations.
    """

    def __init__(self, x, y):
        """
        Initialize a Point object with x and y coordinates.

        :param x: The x-axis coordinate value.
        :param y: The y-axis coordinate value.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return the string representation of the point.

        :return: A string in the form "<x, y>".
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Return the official string representation of the point.

        :return: A string in the form "<x, y>", identical to __str__.
        """
        return self.__str__()

    def distance_orig(self):
        """
        Compute the Euclidean distance of the point from the origin (0, 0).

        :return: The distance as a float.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other):
        """
        Compare this point with another based on their distance from the origin.

        :param other: Another Point object.
        :return: True if this point is farther from the origin than the other.
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        """
        Check equality between this point and another based on their distance from the origin.

        :param other: Another Point object.
        :return: True if both points have the same distance from the origin.
        """
        return self.distance_orig() == other.distance_orig()


if __name__ == "__main__":
    """
    Main execution block:
    - Creates a list of random Point objects.
    - Sorts them based on distance from the origin.
    - Estimates the probability of two randomly generated points having the same distance from the origin.
    """
    points = []
    for i in range(5):
        # create a random point
        p = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        # append it to the list
        points.append(p)

    print("unsorted points")
    print(points)
    print("sorted points")
    points.sort()
    print(points)

    found_equal = 0
    count = 0
    while True:
        if found_equal == 10000:
            break
        p1 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        p2 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        count += 1
        if p1 == p2:
            # print(p1, p2)
            found_equal += 1

    print(f"probability is 1 in {count / found_equal} ")