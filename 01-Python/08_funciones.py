def hola_mundo():  # None
    print("Hola mundo")


print(hola_mundo())


def sumar_dos_numeros(num_uno, num_dos):
    if (num_uno == 1):
        return "Hola"
    else:
        return num_uno + num_dos


print(sumar_dos_numeros(3, 2))


def imprimir_universidad(nombre_universidad="EPN"):
    print(f"{nombre_universidad} es lo maximo")


imprimir_universidad()

imprimir_universidad("Salford")


def guardar_carros(posicion, placa, usuario, tip, color):
    print(f"Guardamos en {posicion} el auto con placa {placa}"
          f"del usuario {usuario}")
    if (color):
        print(f"El color del carro es {color}")
    if (tip):
        print(f"Se recibio un tip de {tip}")


guardar_carros(1, "123-ABC", "Adrian", color="Amarillo", tip=25.53)
guardar_carros(color="Amarillo",
               tip=25.53,
               posicion=1,
               placa="123-ABC",
               usuario="Adrian")


# normales
# defecto or *


def sumar_numeros(resta, *numeros, valor_inicial=0):
    for numero in numeros:
        valor_inicial = valor_inicial + numero
    return valor_inicial - resta


resultado = sumar_numeros(1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 4, valor_inicial=10)

print(resultado)


def imprimir_nombre(normal, *infinito, defecto=1, posicional, **kwargs):  ## key word arguments
    print(f"{kwargs['primer_nombre']} {kwargs['segundo_nombre']} "
          f"{kwargs['apellido_paterno']} {kwargs['apellido_materno']}")


imprimir_nombre(2, 3, 4, 5, 6, 7, 8,
                defecto=2,
                posicional=3,
                primer_nombre="Vicente",
                segundo_nombre="Adrian",
                apellido_paterno="Eguez",
                apellido_materno="Sarzosa")

#  numero = input("Ingrese un numero")

# print(float(numero) + 12.2 + 1)

# opcional = input("Desea papas con su orden, Opc:Si Opc:No")

# if (True if opcional == "Si" else False):
#     print("Truthy")
# else:
#     print("Falsy")

# numeros = input("Ingrese numeros")

# Recibir numeros separados por comas y usar un split

# 1) Recibir numeros -> Validar que sean numeros y que esten separados por coma
#   1.1) separar por coma
#   1.2) sean numeros
# 2) Convertir los elementos de la tupla en Float
# 4) Ejecutar la funcion !!

# Proceso

tupla = (1, 2, 3, 4, 5)

resultado_suma_string = sumar_numeros(0, valor_inicial=0, *tupla)

print(resultado_suma_string)


def calculadora(numero_uno, numero_dos, operacion="suma"):
    def sumar_dos_numeros():
        return numero_uno + numero_dos

    def restar_dos_numeros():
        return numero_uno - numero_dos

    def dividir_dos_numeros():
        return numero_uno / numero_dos

    def multiplicar_dos_numeros():
        return numero_uno * numero_dos

    def switch_operaciones():
        return {
            'suma': sumar_dos_numeros(),
            'resta': restar_dos_numeros(),
            'multiplicacion': multiplicar_dos_numeros(),
            'division': dividir_dos_numeros()
        }[operacion]

    return switch_operaciones()


## registrar clases

## CREAR BORRAR ACTUALIZAR BUSCAR


print(calculadora(8, 2, 'division'))


def leer_archivo(path):
    try:
        archivo_abierto = open(path)  # Defecto es 'r' que significa leer

        arreglo_lineas_archivo = archivo_abierto.readlines()

        for linea in arreglo_lineas_archivo:
            print(linea)

        archivo_abierto.close()


    except Exception:
        print("No se pudo leer el archivo")


def agregar_a_archivo(path, *lineas_a_escribir):
    try:
        archivo_abierto = open(path, 'a')  # 'a' Anade nueva linea

        for linea in lineas_a_escribir:
            archivo_abierto.write("\n"+linea)

        archivo_abierto.close()

    except Exception:
        print("No se pudo leer el archivo")


leer_archivo('./08_ejemplo.txt')
agregar_a_archivo('./08_ejemplo.txt', "Hola esta", "es una", "prueba")
