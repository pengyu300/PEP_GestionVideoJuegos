from diccionarios import (
    leer_videojuego,
    buscar_titulo,
    crear_videojuego,
    eleiminar_videojuego,
    diccionario_videojuegos,
)
from conjuntos import generos


def menu():
    print(
        "GESTIÓN DE VIDEOJUEGOS\n1. Listar videojuegos\2. Buscar videojuegos\n3. Añadir videojuegos\n4. Eliminar videojuegos\n5. Mostrar videojuegos\n6. Salir"
    )


def main():
    menu()
    opcion = int(input("Selecciona una opción : "))
    match opcion:
        case 1:  # Listar videojuegos
            for x in diccionario_videojuegos:
                leer_videojuego(diccionario_videojuegos, diccionario_videojuegos(x))
        case 2:  # Buscar videojuegos
            titulo = input('Introduce el nombre del videojuego que quiere buscar: ')
            buscar_titulo(diccionario_videojuegos, titulo)
        case 3:  # Añadir videojuegos
            titulo = input('Introduce el nombre del videojuego que quieres añadir: ')
            anio = int(input('Introduce el año de publicacion: '))
            genero = input('Introduce el genero del videojuego: ')
            crear_videojuego(titulo, anio, genero.replace(" ", "").split(','))
        case 4:  # Eliminar videojuegos
            titulo = input('Introduce el nombre del videojuego que quieres eliminar: ')
            eleiminar_videojuego(diccionario_videojuegos, titulo)
        case 5:  # Mostrar videojuegos
            generos()
        case 6:  # Salir
            print("FIN")
        case _:
            print("Opción no válida")
            main()


if __name__ == "__main__":
    main()
