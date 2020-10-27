class Estudiante():

    # constructor   es un metodo especial que permite inicializar con un valora a los atributos del objeto
    # el argumento self hace referencia al objeto en sí mismo
    def __init__(self, matri, nom, car):
        self.matricula = matri  # para poder acceder a un atributo de la clase se utiliza self.
        self.nombre = nom
        self.carrera = car
        self.promedio=0.0
        #print("Se acaba de crear un estudiante matricula:{} nombre:{} carrera:{}".format(self.matricula, self.nombre, self.carrera))

    # los metodos: calcularPromedio y   mostrarPromedio
    #  no son especiales por que los define el programador de la clase y no python
    def calcularPromedio(self, cal1, cal2):
        self.promedio = (cal1 + cal2) / 2

    def getPromedio(self):
        return self.promedio

    # método especial str definido por python para mostrar el objeto en cadena
    def __str__(self):
        return "Estudiante matricula:{}  nombre:{}   carrera:{}".format(
            self.matricula, self.nombre,self.carrera)

