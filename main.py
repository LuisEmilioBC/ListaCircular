# Práctica Lista Circular Clase 4

from ListaCircular import ListaCircular
lista = ListaCircular()
numero = 0
opcion = 0

while opcion !=6:
    opcion= int(input("Digite la opcion que requiera: \n"
                      "1. Ingresar \n"
                      "2. Mostrar \n"
                      "3. Buscar \n"
                      "4. Modificar \n"
                      "5. Eliminar \n"
                      "6. Salir \n: "))
    match opcion:
        case 1:
            numero= int(input("Digite el número que desea insertar: "))
            lista.agregar(numero)
        case 2:
            lista.mostrar()
        case 3:
            numero=int(input("Digite el número que desea buscar: "))
            if lista.buscar(numero):
                print("El número se encuentra en la lista")
            else:
                print("El número NO se encuentra en la lista")
        case 4:
            datoActual=int(input("Digite el número que desea modificar: "))
            datoNuevo=int(input("Digite el nuevo número con el que lo desea cambiar: "))
            lista.modificar(datoActual,datoNuevo)
        case 5:
            numero= int(input("Digite el número que desea eliminar: "))
            lista.eliminar(numero)
        case 6:
            print("Saliendo del programa... ")
        case _:
            print("Opción inválida")