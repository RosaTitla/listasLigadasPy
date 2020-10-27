from nodo import Nodo
class ListaLigada:
    def __init__(self):
        self.headval = None

    def mostrarListaLigada(self):
        printval = self.headval
        while printval is not None:
            print(printval.dato)
            printval = printval.siguiente


lista1 = ListaLigada()
lista1.headval = Nodo('lunes')
miNodo2 = Nodo("martes")
miNodo3 = Nodo("miercoles")
# Ligar el primer Nodo al segundo nodo
lista1.headval.siguiente = miNodo2

# Ligar el  segundo Nodo al tercer nodo
miNodo2.siguiente = miNodo3

lista1.mostrarListaLigada()