"""
Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas se lanzaron en cada década y cuál es la duración promedio de cada género de película.

"""

import numpy as np

# array con datos de peliculas
peliculas = np.array(
    [
        ["Peli 1", "Comedia", 120, 1990, 8.5],
        ["Peli 2", "Acción", 110, 2005, 7.8],
        ["Peli 3", "Drama", 95, 2010, 6.9],
        ["Peli 4", "Comedia", 100, 1985, 7.5],
        ["Peli 5", "Acción", 130, 2015, 8.1],
        ["Peli 6", "Drama", 115, 2000, 6.7],
        ["Peli 7", "Comedia", 90, 1995, 8.2],
        ["Peli 8", "Acción", 105, 2010, 7.4],
        ["Peli 9", "Drama", 125, 1980, 6.8],
        ["Peli 10", "Comedia", 95, 2000, 8.0],
    ]
)

# cuál es el género de película más popular

genero = peliculas[:, 1]
duracion = peliculas[:, 2]
año = peliculas[:, 3]

conteo_comedia = 0
conteo_accion = 0
conteo_drama = 0

for i in genero:
    if i == "Comedia":
        conteo_comedia += 1

    if i == "Acción":
        conteo_accion += 1

    if i == "Drama":
        conteo_drama += 1


if conteo_comedia > conteo_accion and conteo_comedia > conteo_drama:
    print(f"El género de películas más popular es Comedia")
elif conteo_accion > conteo_comedia and conteo_accion > conteo_drama:
    print(f"El género de películas más popular es Acción")
elif conteo_drama > conteo_comedia and conteo_drama > conteo_accion:
    print(f"El género de películas más popular es Drama")


# cuántas películas se lanzaron en cada década
decada80 = []
decada90 = []
decada2000 = []
decada2010 = []

for e in año:

    if int(e) >= 1980 and int(e) < 1990:
        decada80.append(e)

    if int(e) >= 1990 and int(e) < 2000:
        decada90.append(e)

    if int(e) >= 2000 and int(e) < 2010:
        decada2000.append(e)

    if int(e) >= 2010 and int(e) < 2020:
        decada2010.append(e)

print(f"Películas lanzadas en los 80s: {len(decada80)}")
print(f"Películas lanzadas en los 90s: {len(decada90)}")
print(f"Películas lanzadas en los 2000s: {len(decada2000)}")
print(f"Películas lanzadas en los 2010s: {len(decada2010)}")

# cuál es la duración promedio de cada género de película

comedia = []
drama = []
accion = []

for p in peliculas:
    if p[1] == "Comedia":
        comedia.append(p)
    if p[1] == "Drama":
        drama.append(p)
    if p[1] == "Accion":
        accion.append(p)

peliculas_comedia = np.array(comedia)
peliculas_drama = np.array(drama)
peliculas_accion = np.array(accion)

# duraciones_comedia = peliculas_comedia[:,2].astype(int).mean()
# duraciones_drama = peliculas_drama[:,2].astype(int)
# duraciones_accion = peliculas_accion[:,2].astype(int)

print(
    f"La duración media de las peliculas de comedia es de {peliculas_comedia[:,2].astype(int).mean()} segundos"
)
print(
    f"La duración media de las peliculas de accion es de {peliculas_accion[:,2].astype(int).mean()} segundos"
)
print(
    f"La duración media de las peliculas de drama es de {peliculas_drama[:,2].astype(int).mean()} segundos"
)
