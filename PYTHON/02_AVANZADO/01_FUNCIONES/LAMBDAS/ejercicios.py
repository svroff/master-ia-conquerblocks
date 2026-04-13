numeros = [4, 7, 10, 13, 18, 21, 24, 31]

# 1) Usa filter + lambda para quedarte solo con los números pares.
# Guarda el resultado en una variable llamada pares.

# 2) Después, usando map + lambda sobre esa lista de pares,
# crea otra lista con cada número multiplicado por 10.
# Guarda el resultado en una variable llamada pares_por_diez.

# 3) Imprime ambas listas.
# ---------------------------------------------------------------------
productos = [
    {"nombre": "ratón", "stock": 15},
    {"nombre": "teclado", "stock": 3},
    {"nombre": "monitor", "stock": 8},
    {"nombre": "portátil", "stock": 2},
]

# 1) Usa filter + lambda para quedarte solo con los productos
# que tengan stock menor que 5.
# Guarda el resultado en una variable llamada poco_stock.

# 2) Usa map + lambda para crear una nueva lista que contenga
# solo los nombres de esos productos.
# Guarda el resultado en una variable llamada nombres_poco_stock.

# 3) Imprime ambas variables.
print("\n------------- PRIMER EJERCICIO -----------------")
pares = list(filter(lambda n: n % 2 == 0, numeros))
pares_por_diez = list(map(lambda n: n * 10, pares))
print(
    f"La lista de pares:\n{pares}\nY la lista de pares multiplicados por 10:\n{pares_por_diez}"
)
print("\n------------- SEGUNDO EJERCICIO -----------------")
poco_stock = list(filter(lambda s: s["stock"] < 5, productos))
print(poco_stock)
nombres_poco_stock = list(map(lambda nombre: nombre["nombre"], poco_stock))
print(nombres_poco_stock)
