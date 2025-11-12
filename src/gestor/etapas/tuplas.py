"""
Representa cada videojuego como una tupla con la forma: (título, año,
género).
 Guarda varias videojuegos en una lista de tuplas.
 Recorre la lista e imprime los datos con un formato claro.
◦ Ejemplo: ‘The Legend of Zelda (1986) Rol’.
"""


def imprimir_tuplas(lista):
    for x in lista:
        print(f"{x[0]} ({x[1]}) {x[2]}")


tupla1 = ("The Legend of Zelda: Tears of the Kingdom", "2023", "Acción y aventura")
tupla2 = ("Hollow Knight: Silksong", "2025", "Metroidvania")
tupla3 = ("Celeste", "2018", "Plataformas")
tupla4 = ("Clair Obscur: Expedition 33", "2025", "Rol")
tupla5 = ("ELDEN RING", "2022", "Rol de acción y aventura")

lista_tuplas_videojuegos = [tupla1, tupla2, tupla3, tupla4, tupla5]
