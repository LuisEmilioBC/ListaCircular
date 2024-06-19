from Nodo import Nodo

class ListaCircular():
    """
    primero : None, Nodo
    ultimo : None, Nodo
    """
    #Método constructor de la clase ListaCircular
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    #Getter del atributo primero (primer elemento)
    def get_primero(self):
        return self.primero
    
    #Setter del atributo primero (primer elemento)
    def set_primero(self,primero):
        self.primero=primero
    
    #Getter del atributo ultimo (ultimo elemento)
    def get_ultimo(self):
        return self.ultimo
    
    #Setter del atributo ultimo (ultimo elemento)
    def set_ultimo(self,ultimo):
        self.ultimo=ultimo
    
    def es_vacia(self):
        return self.primero is None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.set_siguiente(nuevo_nodo)
        self.ultimo = nuevo_nodo
        self.ultimo.set_siguiente(self.primero)
    
    def mostrar(self):
        if self.es_vacia():
            print("La lista está vacía")
            return
        nodo_actual = self.primero
        while True:
            print(nodo_actual.get_dato(), end=" -> ")
            nodo_actual = nodo_actual.get_siguiente()
            if nodo_actual == self.primero:
                break
        print("")
    
    def buscar(self,dato):
        nodoActual = self.primero
        boolean= False
        while True:
            if nodoActual.get_dato()==dato:
                boolean=True
            nodoActual=nodoActual.get_siguiente()
            if nodoActual == self.get_primero():
                break
            
        return boolean
    
    def modificar(self, datoActual, datoNuevo):
        nodoActual = self.primero
        while True:
            if nodoActual.get_dato()==datoActual:
                nodoActual.set_dato(datoNuevo)
                break
            nodoActual=nodoActual.get_siguiente()
            if nodoActual == self.get_primero():
                break
            
    
    def eliminar(self, dato):
        if self.es_vacia():
            print("La lista está vacía. No se puede eliminar.")
            return
        nodo_actual = self.primero
        nodo_anterior = None
        while True:
            if nodo_actual.dato == dato:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                elif nodo_actual.siguiente == nodo_actual:
                    self.primero = None
                    self.ultimo = None
                else:
                    self.primero = nodo_actual.siguiente
                    self.ultimo.siguiente = self.primero
                if nodo_actual == self.ultimo:
                    self.ultimo = nodo_anterior
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        
            
            
    
    