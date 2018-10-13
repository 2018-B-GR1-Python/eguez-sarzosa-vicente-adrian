adrian = {
    'nombre': "Adrian",
    'apellido': 'Eguez',
    "edad": 29,
    "sueldo": 1.01,
    "hijos": [],
    "casado": False,
    "loteria": None,
    "mascota": {
        "nombre": "Cachetes",
        "edad": 3
    },
}
print(adrian)

print(adrian["nombre"])  # Adrian
print(adrian["mascota"]["nombre"])  # Cachetes
print(adrian.get("apellido"))
adrian.pop("casado")
print(adrian)
print(adrian.values())
for valor in adrian.values():
    print(f"Valor: {valor}")

for llave in adrian.keys():
    print(f"Llave: {llave} valor: {adrian.get(llave)}")

for clave, valor in adrian.items():
    print(f"clave: {clave} valor: {valor}")

adrian["profesion"] = "Maistro"
print(adrian)

nuevos_valores = {"peso": 0, "altura": 1}

adrian.update({"peso": 0, "altura": 1})

print(adrian)
