"""
Transforma tu colección en un diccionario donde:
◦ La clave sea un identificador único (título normalizado).
◦ El valor sea otro diccionario con datos del videojuego:
{
    "titulo": str,
    "anio": int,
    "genero": set
}
Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el catálogo.
Implementa funciones de búsqueda:
    - Exacta por título.
    - Parcial (fragmento del título).
    - Por género o rango de años.
Calcula estadísticas:
    - Número total de videojuegos.
    - Conteo por género.
"""
def crear_videojuego(diccionario, titulo, anio, genero):
    clave = titulo.lower().strip()
    if clave in diccionario:
        print("Este videojuego ya existe en el diccionario.")
    else:
        diccionario[clave] = {
            "titulo": titulo.strip(),
            "anio": anio,
            "genero": set(genero),
        }
        print("Videojuego añadido correctamente.")
def leer_videojuego(diccionario, titulo):
    clave = titulo.lower().strip()
    if clave in diccionario:
        vj = diccionario[clave]
        print(
            f"Título: {vj['titulo']} | Año: {vj['anio']} | Género: {', '.join(vj['genero'])}"
        )
    else:
        print("El videojuego no existe en el diccionario.")
def actualizar_videojuego(diccionario, titulo, nuevo_anio, nuevo_genero):
    clave = titulo.lower().strip()
    if clave in diccionario:
        diccionario[clave]["anio"] = nuevo_anio
        diccionario[clave]["genero"] = set(nuevo_genero)
        print("Videojuego actualizado correctamente.")
    else:
        print("El videojuego no existe en el diccionario.")
def eliminar_videojuego(diccionario, titulo):
    clave = titulo.lower().strip()
    if clave in diccionario:
        del diccionario[clave]
        print("Videojuego eliminado correctamente.")
    else:
        print("El videojuego no existe en el diccionario.")
def buscar_titulo(diccionario, titulo):
    leer_videojuego(diccionario, titulo)
def buscar_parcial(diccionario, fragmento):
    encontrado = False
    for vj in diccionario.values():
        if fragmento.lower() in vj["titulo"].lower():
            print(
                f"Título: {vj['titulo']} | Año: {vj['anio']} | Género: {', '.join(vj['genero'])}"
            )
            encontrado = True
    if not encontrado:
        print("No se ha encontrado ningún videojuego que coincida parcialmente.")
def buscar_genero(diccionario, genero):
    encontrado = False
    for vj in diccionario.values():
        if any(genero.lower() == g.lower() for g in vj["genero"]):
            print(
                f"Título: {vj['titulo']} | Año: {vj['anio']} | Género: {', '.join(vj['genero'])}"
            )
            encontrado = True
    if not encontrado:
        print("No se ha encontrado ningún videojuego con ese género.")
def buscar_anio(diccionario, fecha_inicio, fecha_fin):
    encontrado = False
    for vj in diccionario.values():
        if fecha_inicio <= vj["anio"] <= fecha_fin:
            print(
                f"Título: {vj['titulo']} | Año: {vj['anio']} | Género: {', '.join(vj['genero'])}"
            )
            encontrado = True
    if not encontrado:
        print("No se ha encontrado ningún videojuego en ese rango de años.")
# Diccionario inicial de videojuegos
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
    "celeste": {
        "titulo": "Celeste",
        "anio": 2018,
        "genero": {"Plataformas"},
    },
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
