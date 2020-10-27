from nodo import Nodo
from listaEnlazada import ListaLigada
miLista1 = ListaLigada()

#creación del primer nodo
miNodo1=Nodo('lunes')
miLista1.primerNodo=miNodo1
#miLista1.primerNodo = Nodo('lunes')
'''  PASOS PARA CREAR UN NODO
paso 1  creación del segundo nodo
'''

miNodo2 = Nodo("martes")



'''
paso 2 Ligar el primer Nodo al segundo nodo
para esto asignamos la referencia del nodo recien creado
en el atributo siguiente del último nodo en la lista
'''

miLista1.primerNodo.siguiente = miNodo2

#ya creados nodo1 y nodo 2
#nodo 1.siguiente  debe tener la misma referencia que nodo 2
#comprobaremos mostrando el ID

print('referencia de nodo1 campo siguiente',id(miNodo1.siguiente))


print('referencia de Nodo 2',id(miNodo2))

'''
creacion del nodo3 paso 1 y paso 2
'''

miNodo3 = Nodo("miercoles")
'''
Ligar el  segundo Nodo al tercer nodo
para esto asignamos la referencia del nodo recien creado
en el atributo siguiente del último nodo en la lista
'''

miNodo2.siguiente = miNodo3

#invocamos la funcion mostrar
miLista1.mostrarListaLigada()


'''
FUNCION AGREGAR NODO
insertar un nuevo nodo a la lista
'''
miNodo3 = Nodo("Jueves")
miLista1.agregarNodo(miNodo3)

#invocamos la funcion mostrar
miLista1.mostrarListaLigada()

miLista1.eliminarNodo("martes")

#invocamos la funcion mostrar
miLista1.mostrarListaLigada()