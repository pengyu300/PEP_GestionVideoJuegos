"""
Transforma tu colección en un diccionario donde:
◦ La clave sea un identificador único ( título normalizado).
◦ El valor sea otro diccionario con datos de la videojuego.
{
"titulo": str,
"anio": int,
"genero": set
}
 Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el catálogo
usando la clave.
 Implementa funciones de búsqueda:
◦ Exacta por título.
◦ Parcial (contenga un fragmento en el título).
◦ Por género o rango de anios.
 Calcula estadísticas:
◦ Número total de videojuegos.
◦ Conteo por género.
"""


def crear_videojuego(diccionario, titulo, anio, genero):
    if titulo.lower().strip() in diccionario:
        print("Este videojuego ya existe en este diccionario")
    else:
        diccionario[titulo.lower().strip()] = {
            "titulo": titulo.strip(),
            "anio": anio,
            "genero": set(genero),
        }
        print("Videojuego añadido correctamente")


def leer_videojuego(diccionario, titulo):
    if titulo.lower().strip() in diccionario:
        vj = diccionario[titulo.lower().strip()]
        print(
            f"Título: {vj['titulo']} | Año: {vj['anio']} | Género: {', '.join(vj['genero'])}"
        )
    else:
        print("El videojuego no existe en este diccionario")


def actualiza_videojuego(diccionario, titulo, nuevo_anio, nuevo_genero):
    if titulo.lower().strip() in diccionario:
        diccionario[titulo.lower().strip()]["anio"] = nuevo_anio
        diccionario[titulo.lower().strip()]["genero"] = set(nuevo_genero)
        print("Videojuego actualizado correctamente")
    else:
        print("El videojuego no existe en este diccionario")


def eleiminar_videojuego(diccionario, titulo):
    if titulo.lower().strip() in diccionario:
        del diccionario[titulo.lower().strip()]
        print("Videojuego eliminado correctamente")
    else:
        print("El videojuego no existe en este diccionario")


def buscar_titulo(diccionario, titulo):
    leer_videojuego(diccionario, titulo)


def buscar_parcial(diccionario, fragmento):
    encontrado = False
    for x in diccionario.values():
        if fragmento.lower() in x["titulo"].lower():
            print(
                f"Título: {x['titulo']} | Año: {x['anio']} | Género: {', '.join(x['genero'])}"
            )
            encontrado = True
    if not encontrado:
        print("El videojuego no existe en este diccionario")


def buscar_genero(diccionario, genero):
    encontrado = False
    for x, y in diccionario_videojuegos.items():
        for z in y["genero"]:
            if genero.lower() == z.lower():
                print(
                    f"Título: {diccionario_videojuegos[x]['titulo']} | Año: {diccionario_videojuegos[x]['anio']} | Género: {', '.join(diccionario_videojuegos[x]['genero'])}"
                )
                encontrado = True
    if not encontrado:
        print("No hemos encontrado ningun videojuego con ese genero")


def buscar_anio(diccionario, fecha_inicio, fecha_fin):
    encontrado = False
    for x in diccionario.values():
        if fecha_inicio <= x["anio"] and fecha_fin >= x["anio"]:
            print(
                f"Título: {x['titulo']} | Año: {x['anio']} | Género: {', '.join(x['genero'])}"
            )
            encontrado = True
    if not encontrado:
        print("No hemos encontrado ningun videojuego publicado en esas fechas")


diccionario_videojuegos = {
    "the legend of zelda: tears of the kingdom": {
        "titulo": "The Legend of Zelda: Tears of the Kingdom",
        "anio": 2023,
        "genero": {"Accion", "Aventura"},
    },
    "hollow knight: silksong": {
        "titulo": "Hollow Knight: Silksong",
        "anio": 2025,
        "genero": {"Metroidvania"},
    },
    "celeste": {"titulo": "Celeste", "anio": 2018, "genero": {"Plataformas"}},
    "clair obscur: expedition 33": {
        "titulo": "Clair Obscur: Expedition 33",
        "anio": 2025,
        "genero": {"Rol"},
    },
    "elden ring": {
        "titulo": "ELDEN RING",
        "anio": 2022,
        "genero": {"Rol", "Accion", "Aventura"},
    },
}
