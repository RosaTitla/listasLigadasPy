from nodoEstudiante import Estudiante
from listaEnlazadaEstudiante import ListaLigadaEstudiante

miLista1 = ListaLigadaEstudiante()

#creación del primer nodo
miNodoalumno1 = Estudiante("2299", "Pedro", "Nanotecnología")


miLista1.primerNodo=miNodoalumno1

'''  PASOS PARA CREAR UN NODO
paso 1  creación del segundo nodo
'''

miNodoalumno2 = Estudiante("3209", "Ezequiel", "Ing. en IA")



'''
paso 2 Ligar el primer Nodo al segundo nodo
para esto asignamos la referencia del nodo recien creado
en el atributo siguiente del último nodo en la lista
'''

miLista1.primerNodo.siguiente = miNodoalumno2

#ya creados nodo1 y nodo 2
#nodo 1.siguiente  debe tener la misma referencia que nodo 2
#comprobaremos mostrando el ID

print('referencia de nodo1 campo siguiente',id(miNodoalumno1.siguiente))


print('referencia de Nodo 2',id(miNodoalumno2))


'''
creacion del nodo3 paso 1 y paso 2
'''
miNodoalumno3 = Estudiante("3233", "Isaias", "Ing. en Ciencia de datos")

'''
Ligar el  segundo Nodo al tercer nodo
para esto asignamos la referencia del nodo recien creado
en el atributo siguiente del último nodo en la lista
'''

miNodoalumno2.siguiente = miNodoalumno3

#invocamos la funcion mostrar
miLista1.mostrarListaLigada()



'''
FUNCION AGREGAR NODO
insertar un nuevo nodo a la lista
'''
miNodoalumno4 = Estudiante("3119", "Emmanuel", "Ing. en TI")
miLista1.agregarNodo(miNodoalumno4)

print('lista estudiantes')
#invocamos la funcion mostrar
miLista1.mostrarListaLigada()


#invocamos la funcion mostrar
print('lista antes de eliminar')
miLista1.mostrarListaLigada()

#invocamos la funcion eliminar
matri='3233'
miLista1.eliminarNodo(matri)
print('lista despues de eliminar')
#invocamos la funcion mostrar
miLista1.mostrarListaLigada()