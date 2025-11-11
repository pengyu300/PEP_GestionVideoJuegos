from listas import lista_videojuegos, imprimir_lista_numerada, añadir_videojuego_final, eliminar_videojuego
from tuplas import lista_tuplas_videojuegos
from cadenas import buscar_videojuego
from conjuntos import generos

def menu():
    print("GESTIÓN DE VIDEOJUEGOS")
    print("1. Listar videojuegos")
    print("2. Buscar videojuegos")
    print("3. Añadir videojuegos")
    print("4. Eliminar videojuegos")
    print("5. Mostrar videojuegos")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Selecciona una opción : "))
        match opcion:
            case 1:  #Listar videojuegos
                imprimir_lista_numerada(lista_videojuegos)
            case 2:  #Buscar videojuegos
                buscar_videojuego(lista_tuplas_videojuegos)
            case 3:  #Añadir videojuegos
                añadir_videojuego_final(lista_videojuegos)
            case 4:  #Eliminar videojuegos
                eliminar_videojuego(lista_videojuegos)
            case 5:  #Mostrar videojuegos
                generos()
            case 6:  #Salir
                print("FIN")
            case _:
                print("Opción no válida")
            

if __name__ == "__main__":
    main()
