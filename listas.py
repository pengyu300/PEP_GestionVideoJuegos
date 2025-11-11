"""
Crea una lista con los títulos de tus 5 videojuegos favoritos.
 Añade nuevas videojuegos al final de la lista.
 Inserta un videojuego en una posición específica.
 Elimina un videojuego de la lista.
 Recorre la lista e imprime los títulos numerados.
 Muestra la lista ordenada alfabéticamente.
"""


def imprimir(lista):
    for x in range(0, len(lista)):
        print(str(x + 1) + ". " + lista[x])


lista1 = [
    "The Legend of Zelda: Tears of the Kingdom",
    "Hollow Knight: Silksong",
    "Celeste",
    "Clair Obscur: Expedition 33",
    "ELDEN RING",
]
lista1.append("Hades")
lista1[4] = "Cult of the Lamb"
lista1.remove("Cult of the Lamb")

imprimir(lista1)
print("\n")
imprimir(sorted(lista1))
