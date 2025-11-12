"""
Módulo: catalogo.py
-------------------
Contiene las funciones CRUD para gestionar el catálogo de videojuegos.
"""
def crear_videojuego(diccionario, titulo, anio, genero):
    """Crea un nuevo videojuego en el diccionario si no existe."""
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
    """Lee y muestra la información de un videojuego por su título."""
    clave = titulo.lower().strip()
    if clave in diccionario:
        vj = diccionario[clave]
        print(f"Título: {vj['titulo']} | Año: {vj['anio']} | Género: {', '.join(vj['genero'])}")
    else:
        print("El videojuego no existe en el diccionario.")
def actualizar_videojuego(diccionario, titulo, nuevo_anio, nuevo_genero):
    """Actualiza el año y género de un videojuego existente."""
    clave = titulo.lower().strip()
    if clave in diccionario:
        diccionario[clave]["anio"] = nuevo_anio
        diccionario[clave]["genero"] = set(nuevo_genero)
        print("Videojuego actualizado correctamente.")
    else:
        print("El videojuego no existe en el diccionario.")
def eliminar_videojuego(diccionario, titulo):
    """Elimina un videojuego del diccionario."""
    clave = titulo.lower().strip()
    if clave in diccionario:
        del diccionario[clave]
        print("Videojuego eliminado correctamente.")
    else:
        print("El videojuego no existe en el diccionario.")
