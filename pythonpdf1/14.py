import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def euclidean_distance(point1, point2):
    distance = math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)
    return distance

point1 = Point(x=5, y=7)
point2 = Point(x=9, y=10)

distance = euclidean_distance(point1, point2)

print("The Euclidean distance between ({}, {}) and ({}, {}) is: {:.2f}".format(point1.x, point1.y, point2.x, point2.y, distance))