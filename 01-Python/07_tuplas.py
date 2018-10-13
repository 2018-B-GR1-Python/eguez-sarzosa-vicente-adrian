tupla = (1, 2, 3, 2, 3, 3, "a", "b", "c", "c")

print(tupla)
for numero in tupla:
    print(f"Numero {numero}")

print(tupla.index(3))  # Devuelve el indice del valor

print(tupla.count(2))  # Devuelve el numero de repeticiones del valor

print(tupla[0:2])  # 3
print(set(tupla))  # Tupla sin repetidos

for t in set(tupla):
    print(f"Valor: {t}")

# arregloUno = [1, 2, 3]
# arregloDos = [4, 5, 6]

arregloUno = [[1, 2], [3, 4], [5, 6]]
arregloDos = [[7, 8], [9, 10], [11, 12]]

print(arregloUno + arregloDos)
