
from conjuntos import generos
def menu():
    print("GESTIÓN DE VIDEOJUEGOS")
    print("1. Listar videojuegos")
    print("2. Buscar videojuegos")
    print("3. Añadir videojuegos")
    print("4. Eliminar videojuegos")
    print("5. Mostrar videojuegos")
    print("6. Salir")

def elegir():
    while True:
        menu()
        opcion = input("Selecciona una opción : ")

        if opcion == "1":
            print("LISTARIAMOS LOS VIDEOJUEGOS")
        elif opcion == "5":
            generos()
        elif opcion == "6":
            print("FIN")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    elegir()
