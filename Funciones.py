def obtener_lista_palabras() -> list:
    palabra_oculta=["voley"]
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
      
    

def verificar_estado_juego(diccionario_juego:dict)->bool:
    estado={

    }
    pass

def mostrar_palabra_oculta(palabra_oculta:str):
    elemento=palabra_oculta.pop()
    orig=str(elemento)
    letras=list(orig)
    

    
    print(F"Elemento eliminado :{elemento}")
    for i in range(len(palabra_oculta)):
        cadena = "ahorcado"
letras = list(cadena)
print(letras)
    if inten==0:
        print(palabra_oculta[i])

def calcular_puntuacion_final():
    pass

palabra_oculta=["voley"]
elemento=palabra_oculta.pop()
orig=str(elemento)
letras=list(orig)
print(letras)