"""
Crea una lista con los títulos de tus 5 videojuegos favoritos.
 Añade nuevas videojuegos al final de la lista.
 Inserta un videojuego en una posición específica.
 Elimina un videojuego de la lista.
 Recorre la lista e imprime los títulos numerados.
 Muestra la lista ordenada alfabéticamente.
"""


def añadir_videojuego_final(lista):
    nombre_videojuego = input(
        "Introduce el nombre de un videojuego que quieras añadir: "
    )
    lista.append(nombre_videojuego)
    return lista


def añadir_videojuego_posicion(lista):
    posicion = int(
        input("Indroduce la posicion en la que quieres insertar el videojuego: ")
    )
    nombre_videojuego = input(
        "Introduce el nombre de un videojuego que quieras añadir en la posicion "
        + posicion
        + " : "
    )
    lista[posicion](nombre_videojuego)
    return lista


def eliminar_videojuego(lista):
    nombre_videojuego = input(
        "Introduce el nombre del videojuego que quieres eliminar: "
    )
    encontrado = False
    for x in lista:
        if nombre_videojuego.lower().replace(" ", "") == x.lower().replace(" ", ""):
            lista.remove(x)
            encontrado = True
    if not encontrado:
        print("ERROR 404: Not Found")
    return lista


def imprimir_lista_numerada(lista):
    for x in range(0, len(lista)):
        print(str(x + 1) + ". " + lista[x])


def imprimir_lista_ordenada(lista):
    lista.sort()
    for x in lista:
        print(x)


lista_videojuegos = [
    "The Legend of Zelda: Tears of the Kingdom",
    "Hollow Knight: Silksong",
    "Celeste",
    "Clair Obscur: Expedition 33",
    "ELDEN RING",
]
