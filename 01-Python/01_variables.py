print("Hola mundo")
edad: int = 20
sueldo = 1.02
print(edad + int(sueldo))
nombre = "Adrian"  # Comentario
apellido = 'Eguez'
apellido_materno = """Sarzosa"""
print(nombre == apellido)  # True / False
print(apellido == apellido_materno)  # True / False
print(apellido_materno)
print(int(True))  # 1
print(int(False))  # 0
print(str(True))  # "True"
print(str(True))  # "False"

print("adrian eguez".capitalize())  # Adrian eguez
nombre_completo = "adrian eguez".split(" ")  # ["adrian","eguez"]
print(nombre_completo[0].capitalize() + " " + nombre_completo[1].capitalize()) # Adrian Eguez
print("Vicente".isalpha())  # True
print("Vicente10".isalpha())  # False
print("10".isnumeric())  # True
print("Vicente10".isnumeric())  # False
print("Vicente10".isalnum())  # True
print("10".isalnum())  # True
print("Vicente10".isalnum())  # True
print("Mi nombre es {0} {1}".format(nombre_completo[0].capitalize(), "Eguez"))
print(f"Mi nombre es {nombre_completo[0].capitalize()} "
      f"{nombre_completo[1].capitalize()}")
print(r"Saltos de linea ")  # raw
no_existe = None  # null
print(no_existe)





