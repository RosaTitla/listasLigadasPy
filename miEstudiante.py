
# importamos la clase Estudiante que se encuentra en el archivo Estudiante
from Estudiante import Estudiante


# creamos un objeto mialumno de la clase estudiante
# y le enviamos los datos ("3399","Rosa","Nanotecnología") para que sea creado en la memoria

mialumno = Estudiante("3399", "Rosa", "Nanotecnología")


#el método __str__ permite imprimir en formato cadena al objeto

print(mialumno)


# invocamos al metodo calcularPromedio y le enviamos las calificaciones

mialumno.calcularPromedio(10, 8)


# invocamos el metodo mostrarPromedio y mandamos a imprimir en pantalla

print(mialumno.getPromedio())

alumno1 = Estudiante("2299", "Pedro", "Nanotecnología")
alumno2 = Estudiante("3209", "Ezequiel", "Ing. en IA")
alumno3 = Estudiante("3209", "Ezequiel", "Ing. en Ciencia de datos")
alumno4 = Estudiante("3209", "Emmanuel", "Ing. en TI")



listaEstudiantes=[alumno1,alumno2,alumno3]
listaEstudiantes.append(alumno4)
for alum in listaEstudiantes:
    print(alum)

