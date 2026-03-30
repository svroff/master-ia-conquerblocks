print("\n------------- PRIMER EJERCICIO -----------------")
precios = [15, 230, 8, 450, 99, 3, 180]
# Filtra los precios que sean mayores a 100 usando filter + lambda, y guárdalos en una variable llamada caros.
caros = list(filter(lambda n: n > 100, precios))
print(caros)
print("\n------------- SEGUNDO EJERCICIO -----------------")
# Tienes esta lista de palabras:
pythonpalabras = ["python", "java", "go", "rust", "c", "kotlin"]
# Usa map + lambda para convertir todas las palabras a mayúsculas. Guárdalo en palabras_mayus.
# Pista: map funciona igual que filter pero en vez de filtrar, transforma cada elemento. Y los strings tienen un método .upper().
palabras_mayores = list(map(lambda p: p.upper(), pythonpalabras))
print(palabras_mayores)
print("\n------------- TERCER EJERCICIO -----------------")
empleados = [
    {"nombre": "Ana", "salario": 1200},
    {"nombre": "Pedro", "salario": 3500},
    {"nombre": "Sofía", "salario": 2800},
    {"nombre": "Luis", "salario": 900},
]
# Filtra solo los empleados con salario mayor a 2000 usando filter + lambda.
# Pista: cada elemento de la lista es un diccionario. Para acceder al salario de uno sería x["salario"].
filtro = list(filter(lambda sueldo: sueldo["salario"] > 2000, empleados))
print(filtro)
