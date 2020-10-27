from datetime import date

fechaPedido = date(2014, 12, 20)
fechaEntrega = date(2015, 5, 1)

print(id(fechaPedido))  #muestra la referencia  78406
print(id(fechaEntrega))  #muestra la referencia  562108

fechaEnvio=fechaEntrega
#muestra la referencia  562108
print(id(fechaEnvio))


a=[81,82,83]
#se asigna la referencia de a a la variable b
b=a

#a y b muestran la misma referencia  4539982080
print(id(a))
print(id(b))

# de tal manera que si modificamos b también se modifica a
b.append(100)
print('a',a)
print('b', b)

#si queremos crear una copia
import copy
c=copy.deepcopy(b)

#https://nedbatchelder.com/text/names.html