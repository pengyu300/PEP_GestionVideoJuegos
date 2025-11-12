from src.gestor.etapa import listas, tuplas, cadenas, conjuntos, diccionarios
def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Gestión de listas")
    print("2. Gestión de tuplas")
    print("3. Búsqueda con cadenas")
    print("4. Conjuntos")
    print("5. Gestión diccionarios (CRUD y búsqueda)")
    print("6. Salir")
    return input("Elige una opción: ")
def menu_diccionario():
    print("\n--- Gestión Diccionarios Videojuegos ---")
    print("1. Añadir videojuego")
    print("2. Mostrar videojuego")
    print("3. Actualizar videojuego")
    print("4. Eliminar videojuego")
    print("5. Buscar por título exacto")
    print("6. Buscar por fragmento en título")
    print("7. Buscar por género")
    print("8. Buscar por rango de años")
    print("9. Volver al menú principal")
    return input("Elige una opción: ")
def gestion_diccionarios():
    while True:
        opcion = menu_diccionario()
        if opcion == "1":
            titulo = input("Título: ")
            try:
                anio = int(input("Año: "))
            except ValueError:
                print("Año inválido, debe ser un número.")
                continue
            genero = input("Género (separados por coma): ").split(",")
            genero = [g.strip() for g in genero if g.strip()]
            if not genero:
                print("Debe ingresar al menos un género.")
                continue
            diccionarios.crear_videojuego(diccionarios.diccionario_videojuegos, titulo, anio, genero)
        elif opcion == "2":
            titulo = input("Título para mostrar: ")
            diccionarios.leer_videojuego(diccionarios.diccionario_videojuegos, titulo)
        elif opcion == "3":
            titulo = input("Título para actualizar: ")
            try:
                anio = int(input("Nuevo año: "))
            except ValueError:
                print("Año inválido, debe ser un número.")
                continue
            genero = input("Nuevos géneros (separados por coma): ").split(",")
            genero = [g.strip() for g in genero if g.strip()]
            if not genero:
                print("Debe ingresar al menos un género.")
                continue
            diccionarios.actualizar_videojuego(diccionarios.diccionario_videojuegos, titulo, anio, genero)
        elif opcion == "4":
            titulo = input("Título para eliminar: ")
            diccionarios.eliminar_videojuego(diccionarios.diccionario_videojuegos, titulo)
        elif opcion == "5":
            titulo = input("Buscar videojuego por título exacto: ")
            diccionarios.buscar_titulo(diccionarios.diccionario_videojuegos, titulo)
        elif opcion == "6":
            fragmento = input("Buscar videojuego por fragmento en título: ")
            diccionarios.buscar_parcial(diccionarios.diccionario_videojuegos, fragmento)
        elif opcion == "7":
            genero = input("Buscar videojuegos por género: ")
            diccionarios.buscar_genero(diccionarios.diccionario_videojuegos, genero)
        elif opcion == "8":
            try:
                inicio = int(input("Año inicio: "))
                fin = int(input("Año fin: "))
            except ValueError:
                print("Años inválidos, deben ser números.")
                continue
            if inicio > fin:
                print("El año inicio no puede ser mayor que el año fin.")
                continue
            diccionarios.buscar_anio(diccionarios.diccionario_videojuegos, inicio, fin)
        elif opcion == "9":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")
def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            print("\nLista de videojuegos (numerada):")
            listas.imprimir_lista_numerada(listas.lista_videojuegos)
        elif opcion == "2":
            print("\nLista de videojuegos (tuplas):")
            tuplas.imprimir_tuplas(tuplas.lista_tuplas_videojuegos)
        elif opcion == "3":
            cadenas.buscar_videojuego()
        elif opcion == "4":
            conjuntos.generos()
        elif opcion == "5":
            gestion_diccionarios()
        elif opcion == "6":
            print("¡Salido!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
if __name__ == "__main__":
    main()
