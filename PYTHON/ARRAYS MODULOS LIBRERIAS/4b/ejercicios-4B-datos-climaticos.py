'''
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes.
'''
import numpy as np

# conjunto de datos

clima = np.array([
    [20, 70, 1009, 1],
    [21, 60, 1011, 1],
    [22, 40, 1010, 1],
    [18, 75, 1012, 2],
    [21, 60, 1008, 3],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [27, 49, 1007, 5],
    [29, 50, 1007, 5],
    [28, 51, 1007, 5],
    [30, 45, 1005, 6],
    [10, 30, 1005, 6],
    [32, 40, 1002, 7],
    [33, 35, 1001, 8],
    [31, 45, 1003, 9],
    [30, 42, 1001, 9],
    [29, 42, 1002, 9],
    [35, 43, 1001, 9],
    [28, 50, 1006, 10],
    [25, 60, 1010, 11],
    [27, 59, 1012, 11],
    [24, 58, 1011, 11],
    [22, 70, 1011, 12]
])

# temperatura promedio de cada mes

meses = clima[:, 3] # Extrae todos los valores de la columna 3
temperaturas = clima[:, 0] # Extrae todas las temperaturas
temp_mes = np.zeros(12) # Array de 0 con 12 posiciones.

# range de 1 al 12
for i in range(1,13):
    temp_mes[i-1] = np.mean(temperaturas[meses == i]) # restamos -i porque el array empieza en la posición 0.
    print(f'La temperatura promedio del mes {i} fue de {temp_mes[i-1]} grados')
    
# humedad promedio durante todo el año

hum = clima[:, 1]
hum_promedio = int(hum.mean())
print(f'La humedad promedio de todo el año es: {hum_promedio} %')

# presión promedio durante todo el año

pr = clima[:, 2]
pr_promedio = int(pr.mean())
print(f'La presión promedio de todo el año es: {pr_promedio} hPa')