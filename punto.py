from math import sqrt
class Point:
# Point class for representing and manipulating x,y coordinates.
#constructor es un metodo especial que permite
# inicializar con un valor a los atributos del objeto
# el argumento self hace referencia al objeto en sí mismo

    def __init__(self, valX, valY):

        self.x = valX
        self.y = valY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

   # método especial str definido por python para mostrar el objeto en cadena
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def distanciaDesdeOrigen(self):
        return (sqrt((self.x ** 2) + (self.y ** 2)) )



