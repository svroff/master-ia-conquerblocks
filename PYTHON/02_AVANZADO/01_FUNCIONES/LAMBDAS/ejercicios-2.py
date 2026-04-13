# 3) Imprime ambas variables.
print("\n------------- PRIMER EJERCICIO -----------------")
alumnos = [
    {"nombre": "Laura", "nota": 4},
    {"nombre": "Carlos", "nota": 7},
    {"nombre": "Marta", "nota": 9},
    {"nombre": "Javier", "nota": 5},
]

# 1) Usa filter + lambda para quedarte solo con los alumnos aprobados
# (nota mayor o igual a 5). Guarda el resultado en aprobados.

aprobados = list(filter(lambda a: a["nota"] >= 5, alumnos))

# 2) Usa map + lambda para crear una lista solo con los nombres
# de los alumnos aprobados. Guarda el resultado en nombres_aprobados.
nombres_aprobados = list(
    map(lambda alumno: alumno["nombre"], aprobados)
)  # 3) Imprime ambas variables.
print(nombres_aprobados)
print("\n------------- SEGUNDO EJERCICIO -----------------")
temperaturas = [12, 18, 21, 7, 30, 25, 14]

# 1) Filtra las temperaturas mayores o iguales a 20.
# Guarda el resultado en calidas.
calidas = list(filter(lambda t: t >= 20, temperaturas))
# 2) Usa map para convertir esas temperaturas a strings
# del tipo: "21 grados", "30 grados", etc.
# Guarda el resultado en etiquetas.
etiquetas = list(map(lambda temp: f"{temp} grados", calidas))
# 3) Imprime ambas variables
print(etiquetas)
