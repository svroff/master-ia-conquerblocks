import numpy as np

# array con datos de peliculas
peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
    
])
# --------- conteo de géneros ---------
generos, conteos = np.unique(peliculas[:,1], return_counts= True)
#print(conteos)
#print(generos)
# ordenamos los conteos de menor a mayor pero con (::-1) invertimos el orden.
conteos_desc = np.argsort(conteos)[::-1]
#print(conteos_desc)
# conteos_desc tiene un índice y le pasamos el índice al array "generos"
genero_popular = generos[conteos_desc[0]]
print(f'el género más popular es: {genero_popular}')


# agrupamos las peliculas por decada 
años = peliculas[:,3]
# sacamos el valor único de la columna 3 (las fechas)
# dividimos con doble barra para sacarnos la parte entera (sin decimal, es decir, redondeando) y multiplicamos por 10. 
# por ejemplo. 1985 / 10 --> 198.5 ; 1985 // 10 --> 198 * 10 --> 1980 (sacamos la década)
decadas = np.unique(años.astype(int) // 10 * 10) 

# -------- contamos las peliculas en cada decada --------

conteos_decadas = []

for decada in decadas:
    conteo = np.count_nonzero((años.astype(int) >= decada) & (años.astype(int) < decada + 10))
    conteos_decadas.append(conteo)

    print(f'en la década de {decada} hubieron {conteo} peliculas')
    

# -------- duración promedio por género --------
todos_generos = peliculas[:,1]
duraciones = peliculas[:,2]
duracion_media = np.zeros(len(generos))

# calculamos la duración media
for i in range(len(generos)):
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(int))
    print(f'duración media de las peliculas de género {generos[i]} es de {duracion_media[i]} minutos')