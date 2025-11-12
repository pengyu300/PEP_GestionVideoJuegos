def generos():
    genero = {"Accion","Aventura","Rol"}
    companero = {"Terror","Simulacción","Deporte","Aventura"}

    print("GESTIÓN DE GÉNEROS")
    print("Géneros favoritos : ",genero )
    print("Género de tu amigo : ",companero )

    union = genero | companero
    interseccion = genero & companero
    diferencia = genero - companero

    print("Unión : " , union)
    print("Intersección : " , interseccion)
    print("diferencia : ", diferencia)
