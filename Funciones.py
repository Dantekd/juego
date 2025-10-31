from datetime import date

def obtener_lista_palabras() -> list:
    palabra_oculta=["volley"]
    return palabra_oculta


def seleccionar_palabra():
    

    pass    


def guardar_puntuacion()->bool:
    puntos=3



    pass

def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo_len:int, maximo_len:int)->str:
    puntaje=0
    usuario=input("Ingrese su nombre de usuario.")
    letra = input("Ingresa una letra: ").lower()
    if letra == len(palabra_oculta):
        mensaje=print("Correcto")
        for i in range(len(palabra_oculta)):
            if palabra_oculta[i] == letra:
                letras_adivinadas[i] = letra
       
    else:
        mensaje_error=print("Incorrecto ")
      
def calcular_puntuacion_parcial(palabra: str, letras_adivinadas: set, intentos_restantes: int) -> int:
    puntaje = 0
    for letra in letras_adivinadas:
        if letra in palabra:    
            puntaje +=3
        else:
            puntaje -=1
    return puntaje

def verificar_estado_juego(diccionario_juego:dict)->bool:
    estado={

    }
    pass

def mostrar_palabra_oculta(palabra_oculta:str):
    elemento=palabra_oculta.pop(0)
    orig=str(elemento)
    letras=list(orig)
    print(letras)
    palabraoculta = ["_"] * len(letras)
    print(palabraoculta)
    if inten==0:
        print(palabra_oculta[0])

def calcular_puntuacion_final(puntajes_parciales):
    return sum(puntajes_parciales)

def calcular_puntuacion_parcial(letra, acierto):
    return 3 if acierto else -1

¡
