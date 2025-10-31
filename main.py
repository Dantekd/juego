from Funciones import*
def jugar_ahorcado(ingrese_nombre_usuario: str, verficar_estado_juego: bool, calcular_puntuacion_final:int)->None:
    ingresar_nombre_usuario()
    #Aca creamos todas las variables temporales que necesite nuestro juego
    
    while verificar_estado_juego():
        #Jugamos
        #Verificamos si la partida sigue o no
        pass
    
    #Pido el nombre del jugador para guardar la puntuación
    calcular_puntuacion_final()
    guardar_puntuacion()

while intentos > 0 and "_" in letras_adivinadas:
    letra = input("Ingresa una letra: ").lower()

    if letra in palabra_oculta:
        print("Correcto")
        for i in range(len(palabra_oculta)):
            if palabra_oculta[i] == letra:
                letras_adivinadas[i] = letra
        puntos += 3
    else:
        print("Incorrecto ")
        intentos -= 1
        puntos -= 1
