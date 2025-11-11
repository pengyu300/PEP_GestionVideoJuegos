"""
Pide al usuario que escriba el nombre de un videojuego.
 Busca si existe en tu lista de tuplas (ignora mayúsculas y espacios extras).
 Si existe, muestra sus datos con formato: "Título: The Legend of Zelda | Género: Rol | Año: 1986".
 Si no existe, muestra un mensaje adecuado.
 Practica métodos de cadenas (.lower(), .upper(), .replace(), `.split()). .
"""

from tuplas import lista


def imprimir(tupla):
    print("Titulo: " + tupla[0] + " | Genero: " + tupla[1] + " | Año: " + tupla[2])


def buscar_videojuego(lista):
    nombre_videojuego = input("Introduce el nombre de un videojuego: ")
    encontrado = False
    for x in lista:
        if nombre_videojuego.lower().replace(" ", "") == x[0].lower().replace(" ", ""):
            imprimir(x)
            encontrado = True

    if not encontrado:
        print("ERROR 404: Not Found")
