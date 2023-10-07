import math


class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    """

    # Default values for init arguments
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Method can take only self argument
    def reset(self):
        self.move(0, 0)

    # Method can take literal arguments (int, float, str...)
    def move(self, x, y):
        self.x = x
        self.y = y

    # Method taking another instance of same class
    def calculate_distance(self, other_point):
        """
        Calculate the Euclidean distance from one point to another.
        :param other_point: <Point>
        :return: <float>
        """
        return math.sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        )


p1 = Point()
p2 = Point(x=5, y=7)  # Using named parameters

print(p1.calculate_distance(p2))

p1.move(-4, 12)

# Using reference to class to call method, passing Point object as self
print(Point.calculate_distance(p1, p2))
