#importamos la clase nodo
from nodo import Nodo

class ListaLigada:

#constructor, Esta clase sólo tiene un campo primerNodo o header

    def __init__(self):
        self.primerNodo = None

# función para mostrar en pantalla los nodos
    def mostrarListaLigada(self):
        elNodo = self.primerNodo
        while elNodo is not None:
            print(elNodo.dato)

            #asignamos la referencia elNodo.siguiente a la var elNodo
            #para que elNodo vaya tomando el valor de cada nodo y
            # así recorrer  hacia el siguiente nodo


            elNodo = elNodo.siguiente


# Función para agregar un nuevo nodo al final de la lista

    def agregarNodo(self, nuevoDato):
        #creacion de un objeto Nodo
        NuevoNodo = nuevoDato
        #comprobamos si la lista está vacia
        if self.primerNodo is None:
            #si está vacia la lista nuevoNodo será el primer nodo
            self.primerNodo = NuevoNodo
            return  #aquí return me sirve para terminar la función

        #asignamos la referencia del primer nodo
        #a ultimo nodo ya que es el primer y ultimo nodo en la lista
        ultimoNodo = self.primerNodo

                #ultimoNodo es un nodo temporal
                #que me sirve para avanzar en la lista de nodos

        #recorremos la lista para encontrar el último nodo
        #recuerda que el último nodo en la lista
        # en su atributo siguiente tiene asignado None
        #desde su creación en la clase Nodo
        while ultimoNodo.siguiente is not None:
            #mientras no sea el ultimo nodo le asignará la
            #referencia del siguiente para ir avanzando
            ultimoNodo = ultimoNodo.siguiente
        ultimoNodo.siguiente=NuevoNodo

# Función para eliminar el  nodo
# busca al nodo previo al que queremos eliminar
# para asignarle en su campo siguiente la referencia del nodo siguiente
    def eliminarNodo(self, elDato):
        # asignamos el primerNodo de la lista
        # a la var nodoTemp  para colocar el cursor al
        #inicio de la lista de nodos
        nodoTemp = self.primerNodo

        #  verificamos que  la lista no está vacia
        if nodoTemp is not None:

            #si la lista contiene sólo un nodo
            #no habrá nodo previo
            #por lo tanto lo eliminamos al asignarle el valor none


            if nodoTemp.dato == elDato:
                #nodoTemp.siguiente tiene valor none ya que es el
                #unico nodo
                self.primerNodo = nodoTemp.siguiente
                #ya que al principio de esta funcion creamos el nodoTemp
                # entonces tambien lo elimnamos al asignarle none

                nodoTemp = None
                return  #concluimos la función

        # si la lista contiene mas de un nodo
        # buscamos al nodo previo al que queremos eliminar
        # busca en la lista desde el principio
        # y nodoTemp es un nodo que me sirve para recorrer la lista

        while nodoTemp is not None:

            if nodoTemp.dato == elDato:
                # cuando encuentra el nodo a eliminar
                # rompemos el bucle para que prev sea el nodo
                # previo al que queremos eliminar
               break

            #si no se cumplio la condición
            #  a prev  le asignamos la referencia de nodoTemp
            #  para seguir avanzando en la lista
            prev = nodoTemp
            #   asignamos a nodoTemp la referencia del siguiente nodo
            #   pasa a ser el siguiente nodo para seguier avanzando
            nodoTemp = nodoTemp.siguiente

        # en el avance se llega al final y nodoTemp será None
        #por lo tanto termina la función
        # y puede ser que no se encuentre el nodo que queremos eliminar

        if nodoTemp == None:
            return
#asignamos la referencia de prev al siguiente nodo para
        #desligarse del nodo al que queremos eliminar
        prev.siguiente = nodoTemp.siguiente

#eliminamos nodoTemp
        nodoTemp= None