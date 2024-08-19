# doy vuelta los numeros usando una lista
numeros = []
a = int(input("agrear numeros: "))
b = int(input("nro dos: "))
c = int(input("nro tres: "))
numeros.append(a)
numeros.append(b)
numeros.append(c)
print(numeros[::-1])

#--------------------------------------------------------------------------------

numero = int(input("Ingresar un numero de tres digitos: "))
print()#linea de espacio
numero = str(numero)#lo paso a string para poder medir el largo
largoN = len(numero)

# bandera - para cortar en el segundo intento, sin la bandera, solicita indefinidamente ingrese nro
intentos = 0 #miestras el largo sea distinto a 3 suma intentos
while largoN != 3:
    largoN = 0
    print("El valor ingresado es incorrecto")

    if intentos == 2:
        print("Has consumido todo los intetos")
        break

    numero = int(input("Ingresar un numero de tres digitos: "))
    numero = str(numero)#los paso a string para medir el largo
    largoN = len(numero)
    if largoN != 3:
        intentos = intentos + 1

if largoN == 3:
    numero = int(str(numero)[::-1])
    print(f"el nro invertido es: {numero}, el largo es de: {largoN}")

print("El programa sigue...")

#-----------------------------------------------------------------------------------
#mejorado - miemtras intentos < 3 entra en el ciclo, sino else "Has consumido..."
# intentos = 0 #bandera
#
while intentos < 3:
    numero = input("Ingrese un número de tres dígitos: ")
    if len(numero) != 3 or not numero.isdigit():#Devuelve Verdadero si la cadena es una cadena de dígitos
        print("El valor ingresado es incorrecto.")
        intentos += 1
    else:
        numero = int(numero)
        numero_invertido = int(str(numero)[::-1])
        print(f"El número invertido es: {numero_invertido}, el largo es: {len(str(numero_invertido))}")
        break
else:
    print("Has consumido todos los intentos.")

print("El programa sigue...")

# ------------------------------------

import re
from datetime import datetime, timedelta

# Función para verificar el formato de la hora
def verificar_formato_hora(hora):
    patron = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
    return bool(patron.match(hora))

# Solicitar la hora actual al usuario
while True:
    hora_actual = input("Por favor, ingrese la hora actual (en formato HH:MM): ")
    if verificar_formato_hora(hora_actual):
        break
    else:
        print("El formato de la hora es inválido. Por favor, utilice el formato HH:MM.")

# Solicitar la cantidad de horas a sumar
while True:
    try:
        horas_a_sumar = int(input("Por favor, ingrese la cantidad de horas a sumar: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Convertir la hora actual a objeto datetime
hora_actual_dt = datetime.strptime(hora_actual, "%H:%M")

# Sumar las horas especificadas
nueva_hora_dt = hora_actual_dt + timedelta(hours=horas_a_sumar)

# Imprimir la nueva hora
print("La hora después de sumar {} horas es: {}".format(horas_a_sumar, nueva_hora_dt.strftime("%H:%M%H:%M")))

#----------------------------------------------------------------------------------------------------------------
"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no."""

#funcion para saber si un numero es entero o no lo es
def es_entero(num):
    if isinstance(num, int) or num.is_integer():
        return True
    else:
        return False

numero = int(input("Por favor ingrese un numero entero: "))
primo = 0 #bandera

for n in range(1, numero + 1):
    valor = numero /n

    if es_entero(valor) == True:#solo con este if puedo saber si es primo
        primo += 1

    if numero == 1:#cuando llega al nro 1 sale
        break

if primo == 2:
    print(f"Este es un numero primo: {numero}")
else:
    print(f"El Numero {numero} No es Primo")

#-------------------Calular el tiempo de un viaje por tramos------------------------------------------
#el usuario ingresara los minutos que le llevo realizar un tramo, cuando ponga 0 calculara el tiempo

print("Programa que calcula tiempo de viaje")

sumaTiempo = 0 #inicializar la var acumulador para poder usarla en el while
while True:
        duracionTramo = int(input("Ingrese el tiempo que demoro para hacer un tramo nuevo: "))

        sumaTiempo += duracionTramo #uso un acumulador, defino afuera la var

        if duracionTramo == 0:
            break

horas = sumaTiempo // 60 #division entera para calcular horas
minutos = sumaTiempo % 60 #mudulo de sumaTiempo para los minutos
print(f"Tiempo total del viaje: horas {horas} y {minutos} minutos")


#--------------El programa informa si  los años son Bisiesto o no son, y se sale con nro 0------------
while True:
    numeroBiesto = int(input("Ingrese una fecha para saber si año es bisiesto: "))
    if numeroBiesto == 0: #sale con el numero Cero
        print("Salio del programa porque presiono la tecla Cero")
        break

    if numeroBiesto % 4 == 0 and numeroBiesto % 100 == 0: #calculo usando modulo(%) en los if
        print(f"El año No es Bisiesto {numeroBiesto}")

    if numeroBiesto % 4 != 0:
        print(f"El ano No es Bisiesto {numeroBiesto}")

    if numeroBiesto % 4 == 0 and numeroBiesto % 100 != 0:
        print(f"El año Si es Bisiesto {numeroBiesto}")

#-------- 6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un-----------
#----------- triángulo rectángulo - El triangulo se formara con numeros aleatorios -------------------------

import random

numeroArmador = int(input("Por favor ingresa un numero para formar un dibujo de un triangulo: "))

for i in range(1, numeroArmador + 1):
    # Imprime números en cada línea con el for j
    for j in range(i):  # la i determina el salto de linea
        numeroFormador = random.randint(0, 100)
        print(numeroFormador, end=" ")  # end=" " separa los numeros
    print()


#--------------------------------------------------------------------------------------------------------
#La secuencia de Collatz de un número entero se construye de la siguiente forma:
# ● si el número es par, se lo divide por dos;
# ● si es impar, se le multiplica tres y se le suma uno;
# La sucesión termina al llegar a uno.
# Desarrolle un programa que entregue la secuencia de Collatz de un número entero: 3
def esNumeroPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print("Programa que entrega la secuencia Collatz de tres numeros distintos")
numero1 = int(input("Ingrese el primer numero por favor: "))
numero2 = int(input("Ingrese el segundo numero por favor: "))
numero3 = int(input("Ingrese el segundo numero por favor: "))

listaNumero = [numero1, numero2, numero3]

for lNumero in listaNumero:
    num1 = lNumero
    print(num1, end=" ")  # imprimo el numero ingresado por el usuario al inicio
    while not lNumero == 1:
        if esNumeroPar(lNumero) == True:

            lNumero = lNumero // 2

        else:
            lNumero = 3 * lNumero + 1

        print(lNumero, end=" ")# end= " ", pongo los numereros en la misma fila
    print()#cuando termino con el primer literal, salto de linea




#--8----Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
# respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
# $50 y $100.

import random

'''dar el vuelto con monedas de 10, 50, 100
usara la monedad que corresponda sin pasarse del calculo'''
def dar_vuelto(vuelto):
    valor = 0
    # cambio = 0
    while valor < vuelto:
        opciones = [10, 50, 100]
        cambio = random.choice(opciones)
        calculo = vuelto - valor
        if cambio <= calculo:
            valor += cambio
            print(cambio)
        # else: este codigo es redundate
        #     cambio = 0

'''calcula el vuelto, 
toma como referencia el precio de A, B, C'''
def calcular_vuelto(precio):
    moneda = 0
    while moneda < precio:
        moneda += int(input("Ingresa una moneda: "))
    return moneda - precio


precio_por_articulo = {
    "A": 270,
    "B": 340,
    "C": 390
}

ingreso = input("Por favor seleccione el tipo de alimentos: A o B o C: ").capitalize()#paso a Mayuscla si es minuscula

if ingreso in precio_por_articulo:
    vuelto = calcular_vuelto(precio_por_articulo[ingreso])
    print(f"El vuelto es: {vuelto} el articulo es: {ingreso} el precio: {precio_por_articulo[ingreso]}")
    dar_vuelto(vuelto)
else:
    print("Opcion no valida")


#--9--------Anagrama. Escribe una función que reciba dos palabras y retorne
# verdadero o falso según sean o no anagramas.

palabra1 = input("Ingresa la primera palabra, para verificar si es un anagrama: ")
palabra2 = input("Ingresa la segunda palabra, para verificar si es un anagrama: ")

largo1 = len(palabra1)
largo2 = len(palabra2)

bandera = False

if largo1 == largo2:
    if palabra1 != palabra2:
        print(f"la palabra {palabra2} es un Anagrama")
        bandera = True
        resultado = [palabra1, palabra2, bandera]
        for columna in resultado:
            print(columna)
    else:
        print(f"la palabra {palabra1} no es un anagrama")

else:
    print("Estas palabras debe contener la misma cantidad de caracteres")



#10----------un programa que reciba como entrada las posiciones en el tablero de un alfil y de
#una torre, e indique cuál pieza captura a la otra:-----------------------------------------------------

def captura_alfil_torre(pos_alfil, pos_torre):
    # Extraer filas y columnas de las posiciones
    alfil_fila, alfil_columna = pos_alfil
    torre_fila, torre_columna = pos_torre

    # Verificar si la torre captura al alfil
    if alfil_fila == torre_fila or alfil_columna == torre_columna:
        return "La torre captura al alfil"

    # Verificar si el alfil captura a la torre-
    '''La función abs() devuelve el valor absoluto de un número.
    distancia desde cero en la recta numérica,sin considerar su signo.'''
    if abs(alfil_fila - torre_fila) == abs(alfil_columna - torre_columna):
        return "El alfil captura a la torre"

    return "Ninguna pieza captura a la otra"


afil_fila = int(input("Ingrese la posicion FILA del afil: "))
afil_columna = int(input("Ingrese la posicion COLUMNA del afil: "))
torre_fila = int(input("Ingrese la posicion FILA de la torre: "))
torre_columna = int(input("Ingrese la posicion COLUMNA de la torre: "))

lista1 = [afil_fila, afil_columna]
lista2 = [torre_fila, torre_columna]

# Ejemplo de uso
pos_alfil = lista1#(3,5)#int(input("ingresa alfil"))
pos_torre = lista2#(5,5)#int(input("ingresa torre"))


resultado = captura_alfil_torre(pos_alfil, pos_torre)
print(f"{resultado}\nFila alfil: {afil_fila}\nColumna alfil: {afil_columna}"
      f"\nFila torre: {torre_fila}\nColumna torre: {torre_columna}")
if resultado == "La torre captura al alfil":
    print("Torre captura")
if resultado == "El alfil captura a la torre":
    print("Alfil captura")
else:
    print("Ninguna Captura")




#piedra paple y tijera--------------------------------------------------------------------------------

# print("Piedra, Papel, Tijera")
#
# '''tijera le gana a papel, papel le gana a
# piedra, piedra le gana a tijera,'''
#
#
#
# bandera = 0
# punto_jugA = 0
# punto_jugB = 0
# puntoUno = 1
# puntoCero = 0
# while bandera < 3:
#     jugadorA = input("Ingrese la jugada A: ")
#     jugadorB = input("Ingrese la jugada B: ")
#     if jugadorA == "tijera" and jugadorB == "papel":
#         print(puntoUno, puntoCero)
#         bandera += 1
#         punto_jugA += 1
#     if jugadorB == "tijera" and jugadorA == "papel":
#         print(puntoCero, puntoUno)
#         bandera += 1
#         punto_jugB += 1
#     if jugadorA == "papel" and jugadorB == "piedra":
#         print(puntoUno, puntoCero)
#         bandera += 1
#         punto_jugA += 1
#     if jugadorB == "papel" and jugadorA == "piedra":
#         print(puntoCero, puntoUno)
#         bandera += 1
#         punto_jugB += 1
#     if jugadorA == "piedra" and jugadorB == "tijera":
#         print(puntoUno, puntoCero)
#         bandera += 1
#         punto_jugA += 1
#     if jugadorB == "piedra" and jugadorA == "tijera":
#         print(puntoCero, puntoUno)
#         bandera += 1
#         punto_jugB += 1
#     else:
#         print(puntoCero, puntoCero)
#
# if punto_jugA == 3:
#     print("gana jugador A")
# else:
#     print("gana judador B")


'''Acceso al diccionario: reglas[jugadorA] obtiene el valor asociado a la clave jugadorA
 en el diccionario reglas. Este valor es la jugada a la que jugadorA le gana.
reglas['piedra'] == 'tijera'  # Esto es True'''

print("Piedra, Papel, Tijera")
def resultado_jugada(jugadorA, jugadorB):
    reglas = {
        'tijera': 'papel',
        'papel': 'piedra',
        'piedra': 'tijera'
    }
    if jugadorA == jugadorB:
        return 0
    elif reglas[jugadorA] == jugadorB:#compara en el dicionario ej piedra : tijera entonces A gana
        return 1
    else:
        return -1 #jugadorB gana


punto_jugA = 0
punto_jugB = 0

while punto_jugA < 3 and punto_jugB < 3:
    jugadorA = input("Ingrese la jugada A: ")
    judadorB = input("Ingrese la jugada B: ")

    resultado = resultado_jugada(jugadorA, judadorB)

    if resultado == 1:
        print(1, 0)
        punto_jugA += 1
    elif resultado == -1:
        print(0, 1)
        punto_jugB += 1
    else:
        print(0, 0)

if punto_jugA == 3:
    print("Gana jugador A")
else:
    print("Gana jugador B")


#12- Torneo de Tenis - Version 1

import random

lista_de_jugadores = []
contador = 1

while contador <= 8:
    jugador = input("Ingrese jugador {}: ".format(contador)) #formatea la cadena
    lista_de_jugadores.append(jugador) #añadimos a la lista
    contador += 1

print("Ronda 1")

# Mezclamos aleatoriamente la lista
random.shuffle(lista_de_jugadores)

# Crear una lista para ganadores
segunda_ronda_ganadores = []
tercera_ronda_ganadores = []
campeon = []

indice = 0
while indice < len(lista_de_jugadores):
    if indice + 1 < len(lista_de_jugadores):#sumo 1 para empezar con numero positivo y al finalizar no quede igual a 8
        jugador_A = lista_de_jugadores[indice]
        jugador_B = lista_de_jugadores[indice + 1]
        print("Grupo {}: (A){} y (B){}".format((indice // 2) + 1, jugador_A, jugador_B))

        ganador = input("ingrese la letra del ganador (A/B): ").upper()

        while ganador not in['A', 'B']:
            ganador = input("ingrese la letra del ganador (A/B): ").upper()

        if ganador == 'A':
            segunda_ronda_ganadores.append(jugador_A)
        else:
            segunda_ronda_ganadores.append(jugador_B)
    else:
        print("Jugador sin pareja:", lista_de_jugadores[indice])
        segunda_ronda_ganadores.append(lista_de_jugadores[indice])

    indice += 2

print("Ganadores de la ronda 1:", segunda_ronda_ganadores)

#Segunda Ronda#####################################################
print("Ronda 2")
# Mezclamos aleatoriamente la lista
random.shuffle(segunda_ronda_ganadores)

indice2 = 0
while indice2 < len(segunda_ronda_ganadores):
    if indice2 + 1 <len(segunda_ronda_ganadores):
        jugador_A = segunda_ronda_ganadores[indice2]
        jugador_B = segunda_ronda_ganadores[indice2 + 1]
        print("Grupo {}: (A){} y (B){}".format((indice2 // 2) + 1, jugador_A, jugador_B))

        ganador = input("ingrese la letra del ganador (A/B): ").upper()

        while ganador not in['A','B']:
            ganador = input("ingrese la letra del ganador (A/B): ").upper()

        if ganador == 'A':
            tercera_ronda_ganadores.append(jugador_A)
        else:
            tercera_ronda_ganadores.append(jugador_B)
    else:
        print("jugador sin pareje:", segunda_ronda_ganadores[indice2])
        tercera_ronda_ganadores.append(segunda_ronda_ganadores[indice2])

    indice2 += 2

print("Ganadores de la ronda 2.", tercera_ronda_ganadores)

print("Ronda 3")

jugador_A = tercera_ronda_ganadores[0]
jugador_B = tercera_ronda_ganadores[1]

print("Grupo {}: (A){} y (B){}".format(3,jugador_A, jugador_B))

ganador = input("ingrese la letra del ganador (A/B): ").upper()

while ganador not in ['A', 'B']:
    ganador = input("ingrese la letra del ganador (A/B): ").upper()

if ganador == 'A':
    campeon = jugador_A
else:
    campeon = jugador_B

print("El Campeon es: ", campeon)

##############################################################################################
#version 2

import random

# Función para validar la entrada del ganador
def obtener_ganador():
    while True:
        ganador = input("Ingrese la letra del ganador (A/B): ").strip().upper()
        if ganador in ['A', 'B']:
            return ganador
        else:
            print("Opción inválida. Por favor ingrese 'A' o 'B'.")

# Ingreso de jugadores
lista_de_jugadores = []
for i in range(1, 9):
    jugador = input("Ingrese jugador {}: ".format(i))
    lista_de_jugadores.append(jugador)

# Ronda 1
print("\nRonda 1")
random.shuffle(lista_de_jugadores)
segunda_ronda_ganadores = []

for i in range(0, len(lista_de_jugadores), 2):
    jugador_A = lista_de_jugadores[i]
    jugador_B = lista_de_jugadores[i + 1] if i + 1 < len(lista_de_jugadores) else "Ninguno"
    print(f"Grupo {i // 2 + 1}: (A) {jugador_A} y (B) {jugador_B}")

    ganador = obtener_ganador()
    segunda_ronda_ganadores.append(jugador_A if ganador == 'A' else jugador_B)

print("\nGanadores de la ronda 1:", segunda_ronda_ganadores)

# Ronda 2
print("\nRonda 2")
random.shuffle(segunda_ronda_ganadores)
tercera_ronda_ganadores = []

for i in range(0, len(segunda_ronda_ganadores), 2):
    jugador_A = segunda_ronda_ganadores[i]
    jugador_B = segunda_ronda_ganadores[i + 1] if i + 1 < len(segunda_ronda_ganadores) else "Ninguno"
    print(f"Grupo {i // 2 + 1}: (A) {jugador_A} y (B) {jugador_B}")

    ganador = obtener_ganador()
    tercera_ronda_ganadores.append(jugador_A if ganador == 'A' else jugador_B)

print("\nGanadores de la ronda 2:", tercera_ronda_ganadores)

# Ronda 3
print("\nRonda 3")
jugador_A = tercera_ronda_ganadores[0]
jugador_B = tercera_ronda_ganadores[1]
print(f"Grupo 3: (A) {jugador_A} y (B) {jugador_B}")

ganador = obtener_ganador()
campeon = jugador_A if ganador == 'A' else jugador_B

print("\nEl Campeón es:", campeon)





# Version 1. Ejerciocio nro 13: El diccionario países asocia cada persona
# con el conjunto de los países que ha visitado:
#INTERACCION entre Diccionarios

paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}


def intersección(a, b):
    # Creamos un conjunto vacío para almacenar la intersección
    resultado = set()

    # Iteramos sobre los elementos del primer conjunto
    for elem in a:
        # Si el elemento está presente en ambos conjuntos, lo agregamos al conjunto de resultado
        if elem in b:
            resultado.add(elem)

    return resultado


# solicito ingrese nombres
a = input("Ingrese primer nombre: ")
b = input("Ingrese segundo nombre: ")

#indico la clave del diccionario con paises[a] ej.
a = paises[a]
b = paises[b]

print(f'el pais en comun es: {intersección(a, b)}')



#Version 2 --Ejercicio 13: intersección----------------------------------------------------

paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}


def cuantos_en_comun(a, b):
    # Verificamos si ambos nombres están en el diccionario
    if a in paises and b in paises:
        # Obtenemos los conjuntos de países visitados por cada persona
        paises_a = paises[a]
        paises_b = paises[b]

        # Encontramos la intersección de los conjuntos
        paises_en_comun = paises_a.intersection(paises_b)

        # Devolvemos la cantidad de países en común,
        # Convertimos el conjunto a una lista y luego a una cadena separada por comas,
        # Solo me da el nombre, sin llaves
        return ', '.join(paises_en_comun)

    else:
        # Si alguno de los nombres no está en el diccionario
        print("Uno o ambos nombres no están en la lista de países visitados.")
        return 0


#solicito ingresar los nombre para comparar
a = input("Ingrese primer nombre: ")
b = input("Ingrese segundo nombre: ")


# Ejemplos de uso de la función
print(f'Los paises en comun son: {cuantos_en_comun(a, b)}')



#Ejercicio14------------- Signo zodiacal.--------------------------------------------------------

signos = {
    'aries': ((3, 21), (4, 20)),
    'tauro': ((4, 21), (5, 21)),
    'geminis': ((5, 22), (6, 21)),
    'cancer': ((6,22), (7, 23)),
    'leo': ((7, 24), (8, 23)),
    'virgo': ((8, 24), (9, 23)),
    'libra': ((9, 24), (10, 23)),
    'escorpio': ((10, 24), (11, 22)),
    'sagitario': ((11, 23), (12, 21)),
    'capricornio': ((12, 22), (1, 20)),
    'acuario': ((1, 21), (2, 19)),
    'piscis': ((2, 20), (3, 20))
}

def retornar_signo_sodiacal(dia,mes):

    for signo, (inicio, fin) in signos.items():
        inicio_mes, inicio_dia = inicio
        fin_mes, fin_dia = fin

        if mes == inicio_mes:
            if dia >= inicio_dia:
                return signo
        if mes == fin_mes:
            if dia <= fin_dia:
                return signo

    return None  # Manejo de casos donde no se encuentre ningún signo (opcional)

dia = int(input("Ingresa el dia de tu Cumpleaños (ej. 01) "))
mes = int(input("Ingrese el mes de tu Cumpleaños (ej.01) "))
while dia > 31 or mes > 12:
    dia = int(input("Ingresa el dia de tu Cumpleaños (ej. 01) "))
    mes = int(input("Ingrese el mes de tu Cumpleaños (ej.01) "))


print(f'Tu signo del Sodiaco es: {retornar_signo_sodiacal(dia, mes)}')




#Ejercicio 15- Autores de Libros.--------------------------------------------------------------------------

libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'Willian Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
    # ...
]

autores = {
    #autor: nacimiento, defuncion, idioma
    'Willian Shakespeare':((1564, 4, 26), (1616, 5, 3), 'ingles'),
    'Franz Kafka':        ((1883, 7, 3), (1924, 6, 3), 'aleman'),
    'Marcela Paz':        ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español')
    # ...
}


def obtener_autor(titulo):

    for ti in libros:
        if ti[0] == titulo:
            return ti[1]


def obtener_idioma(titulo):

    autor = obtener_autor(titulo)

    for key in autores.keys():
        if autor in key:

            for llaves, valor in autores.items():
                if llaves == key:
                    return valor[2]


def calcular_annos_antes_de_morir(titulo):

    autor1 = obtener_autor(titulo)
    for ti1 in libros:
        if ti1[1] == autor1:
            ano = ti1[2]

            for llaves2, valor2 in autores.items():
                if llaves2 == autor1:
                    ano_fallecido = valor2[1][0]
                    return ano_fallecido - ano


titulo = input('Ingrese titulo del libro: ')
print('El libro fue escrito en', obtener_idioma(titulo))
print('por el autor:',obtener_autor(titulo))
print('El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años',
       'despues de haber escrito el libro')




#Ejercicio 16---Codigo Morce

import re

morce = {
    'A': ('.-'),
    'B': ('-...'),
    'C': ('-.-.'),
    'CH': ('----'),
    'D': ('-..'),
    'E': ('.'),
    'F': ('..-.'),
    'G': ('--.'),
    'H': ('....'),
    'I': ('..'),
    'J': ('.---'),
    'K': ('-.-'),
    'L': ('.-..'),
    'M': ('--'),
    'N': ('-.'),
    'Ñ': ('--.--'),
    'O': ('---'),
    'P': ('.--.'),
    'Q': ('--.-'),
    'R': ('.-.'),
    'S': ('...'),
    'T': ('-'),
    'U': ('..-'),
    'V': ('...-'),
    'W': ('.--'),
    'X': ('-..-'),
    'Y': ('-.--'),
    'Z': ('--..'),
    '0': ('-----'),
    '1': ('.----'),
    '2': ('..---'),
    '3': ('...--'),
    '4': ('....-'),
    '5': ('.....'),
    '6': ('-....'),
    '7': ('--...'),
    '8': ('---..'),
    '9': ('----.'),
    '.': ('.-.-.-'),
    ',': ('--..--'),
    '?': ('..--..'),
    '"': ('.-..-.'),
    '/': ('-..-.')
}


traducir = []
traducir = input("Ingrese un cadena de texto o morce 'este separados por espacios', para convertir: ")
traducir = traducir.upper()

if re.search(r'[a,zA-Z]', traducir):

    for traduce in traducir:
        for letra in morce.items():
            if traduce == letra[0]:
                resultado = letra[1]
                print(resultado, end=' ')

else:
# split()divide la cadena en una lista de subcadenas usando el espacio como delimitador
    partes = traducir.split()

    resul = ["" + parte + "" for parte in partes]

    for par in resul:
        for llave, mor in morce.items():
            if par == mor:
                print(llave, end='')









































