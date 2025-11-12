#normaliza un texto para búsqueda
def normalizar_texto(texto):
    if texto is None:
        return ""
    # Quita espacios al principio y final
    texto_limpio = texto.strip()
    # Convierte a minúsculas
    texto_minusculas = texto_limpio.lower()
    return texto_minusculas

#formatea un título con la primera letra en mayuscula
def formatear_titulo(texto):
    if not texto:
        return texto
    texto_limpio = texto.strip()
    if len(texto_limpio) > 0:
        # Pone la primera letra en mayúscula y el resto en minúscula
        return texto_limpio[0].upper() + texto_limpio[1:].lower()
    return texto_limpio

#valida que la opción del menú sea correcta
def validar_opcion_menu():
    while True:
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":
            return opcion
        else:
            print("Opcion no valida. Elige un numero del 1 al 6")

#valida que el año sea un número entre 1950 y 2025
def validar_ano():
    while True:
        ano_texto = input("Año del videojuego: ")
        
        # Verificar si todos los caracteres son números
        es_numero = True
        for caracter in ano_texto:
            if caracter not in "0123456789":
                es_numero = False
                break
        
        if not es_numero:
            print("Por favor, introduce un año valido (solo numeros)")
            continue
        
        # Convertir a número
        ano_numero = int(ano_texto)
        
        # Verificar rango del año
        if ano_numero >= 1950 and ano_numero <= 2024:
            return ano_numero
        else:
            print("El año debe estar entre 1950 y 2024")

#valida que el texto no esté vacío
def validar_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje)
        texto_limpio = texto.strip()
        if texto_limpio != "":
            return texto_limpio
        else:
            print("Este campo no puede estar vacio")

#muestra un encabezado formateado
def mostrar_encabezado(titulo):
    print("========================================")
    print("   " + titulo)
    print("========================================")

#mostrar un mensaje de éxito
def mostrar_mensaje_exito(mensaje):
    print("EXITO: " + mensaje)

#muestra un mensaje de error
def mostrar_mensaje_error(mensaje):
    print("ERROR: " + mensaje)

#nuestra un mensaje informativo
def mostrar_mensaje_info(mensaje):
    """
    Muestra un mensaje informativo
    """
    print("INFO: " + mensaje)

#formatea la información de un videojuego para mostrar
def formatear_info_videojuego(juego):
    if juego is None:
        return "No hay informacion del videojuego"
    
    titulo = juego.get('titulo', 'Desconocido')
    ano = juego.get('ano', 'Desconocido')
    genero = juego.get('genero', 'Desconocido')
    
    return "Titulo: " + str(titulo) + " | Año: " + str(ano) + " | Genero: " + str(genero)

#pausa el programa hasta que el usuario presione Enter
def pausar_y_continuar():
    input("Presiona Enter para continuar...")

#pide confirmación para una acción (si/no)
def confirmar_accion(mensaje):
    while True:
        respuesta = input(mensaje + " (si/no): ")
        respuesta_minusculas = respuesta.lower()
        if respuesta_minusculas == "si" or respuesta_minusculas == "s":
            return True
        elif respuesta_minusculas == "no" or respuesta_minusculas == "n":
            return False
        else:
            print("Por favor, responde con 'si' o 'no'")

# Ejemplo de uso para probar las funciones
if __name__ == "__main__":
    print("Probando funciones de utils_texto.py:")
    
    # Probar normalizar_texto
    texto_prueba = "   The Legend OF ZELDA   "
    resultado = normalizar_texto(texto_prueba)
    print("Normalizar texto: '" + texto_prueba + "' -> '" + resultado + "'")
    
    # Probar formatear_titulo
    resultado2 = formatear_titulo(texto_prueba)
    print("Formatear titulo: '" + texto_prueba + "' -> '" + resultado2 + "'")
    
    # Probar formatear_info_videojuego
    juego_ejemplo = {"titulo": "Super Mario", "ano": 1985, "genero": "Plataformas"}
    resultado3 = formatear_info_videojuego(juego_ejemplo)
    print("Formatear videojuego: " + resultado3)
    
    mostrar_mensaje_exito("Funciones probadas correctamente")
