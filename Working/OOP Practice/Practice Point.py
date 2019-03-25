class Point():

    def __init__(self, px, py):
        self.x = px
        self.y = py

    def get_distance(self, other_point):
        """
        Get distance between two points
        :param other_point: other point
        :return: distance between points
        """
        return ((abs(self.x - other_point.x)**2 + abs(self.y - other_point.y)**2)**0.5)

def main():
    p1 = Point(5, 10)
    p2 = Point(3, 4)

    print p1.get_distance(p2)

main()