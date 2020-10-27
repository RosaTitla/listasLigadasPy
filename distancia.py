from punto import Point
from math import sqrt

def distance(point1, point2):
    xdif = point2.getX()-point1.getX()
    ydif = point2.getY()-point1.getY()

    dist = sqrt(xdif**2 + ydif**2)
    return dist

p = Point(4,3)
q = Point(0,0)
print('distancia entre 2 puntos',distance(p,q))


