arreglo = []

arregloCosas = [
    "a",
    1,
    True,
    False,
    None,
    10.1,
    [1, 2, 3]
]

arregloNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0,3[
print(arregloNumeros[0:5])
print(arregloNumeros[3:5])
print(arregloNumeros[:2])
print(arregloNumeros[2:])
print(arregloNumeros[-1])
print(arregloNumeros[-2])
print(arregloNumeros[3:-2])
print(arregloNumeros[-5:-2])

print(7 in arregloNumeros)
print(15 in arregloNumeros)
print(len(arregloNumeros))

arregloNumeros.append(10)
print(arregloNumeros)
arregloNumeros.pop(-3)
print(arregloNumeros)
arregloNumeros.insert(1, 1.1)
print(arregloNumeros)
del arregloNumeros[1:4]
print(arregloNumeros)
