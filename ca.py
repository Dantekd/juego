
def jugar_ahorcado():
    lista_palabras = obtener_lista_palabras()
    palabra = seleccionar_palabra(lista_palabras)

    palabraoculta = [""] * len(palabra)
    intentos_restantes = 7
    puntaje_total = 0

    while True:
        mostrar_palabra_oculta(palabra, palabra_oculta)
        letra = input("Ingresa una letra: ").lower()
        palabra_oculta, acierto = actualizar_palabra_oculta(palabra, palabra_oculta, letra)

        if not acierto:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Intentos restantes: {intentos_restantes}")
cadena = "ahorcado"
letras = list(cadena)
print(letras)