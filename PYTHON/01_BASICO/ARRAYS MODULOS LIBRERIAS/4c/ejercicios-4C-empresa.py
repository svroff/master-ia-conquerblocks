"""
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente.


(Pista 2: puede ser util investigar np.unique y np.argmax)
"""

import numpy as np
import test

datos = np.array(
    [
        ["2022-01-01", "Componente 1", "Lote A", 80],
        ["2022-01-15", "Componente 1", "Lote B", 90],
        ["2022-02-01", "Componente 2", "Lote C", 85],
        ["2022-02-15", "Componente 2", "Lote D", 95],
        ["2022-03-01", "Componente 1", "Lote E", 75],
        ["2022-03-15", "Componente 2", "Lote F", 90],
        ["2022-03-18", "Componente 3", "Lote G", 92],
        ["2022-03-21", "Componente 3", "Lote H", 91],
        ["2022-04-13", "Componente 3", "Lote I", 78],
    ]
)

# aislo cada columna
fechas = datos[:, 0]
componentes = datos[:, 1]
lotes = datos[:, 2]
puntuaciones = datos[:, 3].astype(int)

# ------------ Ejercicios --------------

# item con la puntuación más alta
puntuacion_mas_alta = puntuaciones.argmax()
tipo_componente_mejor = componentes[puntuacion_mas_alta]
"""print(
    f"el tipo de componente con la puntuación de calidad más alta es: {tipo_componente_mejor} con una puntuación de {puntuaciones[puntuacion_mas_alta]}"
)"""

# item con la puntuación más baja con su fecha.
puntuacion_mas_baja_indice = puntuaciones.argmin()
puntuacion_mas_baja = puntuaciones[puntuacion_mas_baja_indice]
fecha_puntuacion_menor = fechas[puntuacion_mas_baja_indice]
"""print(
    f"El componente con la puntuacion más baja ({puntuacion_mas_baja}) se fabricó en {fecha_puntuacion_menor} "
)"""

# todos los items que tienen menos de 80 puntos.

mascara_calidad = puntuaciones < 80
peores_componentes = lotes[mascara_calidad]
fechas_peores_componentes = fechas[mascara_calidad]
peores_puntuaciones = puntuaciones[mascara_calidad]

"""print(
    f"El componente con la peor puntuacion es el {peores_componentes}, con fecha {fechas_peores_componentes} y la puntuacion de {peores_puntuaciones}"
)"""

# componentes que sean 'componente 1' y su puntuacion sea mayor a 70

mascara_calidad_1 = (puntuaciones > 70) & (componentes == "Componente 1")
puntuaciones_mascara = puntuaciones[mascara_calidad_1]
lotes_mascara = lotes[mascara_calidad_1]
"""
print(
    f"Los lotes que son Componente 1 con una puntuación superior a 70 son: {lotes_mascara} con una puntuacion de {puntuaciones_mascara}"
)
"""

# ------------ cuántos componentes se produjeron en cada mes
formato_fechas = fechas.astype("datetime64")
fechas_en_meses = formato_fechas.astype("datetime64[M]")  # cogemos solo los meses

meses_unicos, cantidad_por_mes = np.unique(fechas_en_meses, return_counts=True)
"""for mes, cantidad in zip(meses_unicos, cantidad_por_mes):
    print(f"En el mes {mes} se produjeron {cantidad} componentes")"""

# ------------ cuál es la puntuación de calidad promedio de cada tipo de componente
"""componentes_unicos = np.unique(componentes)
print(f"Hay los siguientes componentes: {componentes_unicos}")

for c in componentes_unicos:
    mask_componentes = componentes == c
    calidad_promedio = np.mean(puntuaciones[mask_componentes])
    max_puntuacion = np.max(puntuaciones[mask_componentes])
    print(f"La calidad promedio de {c} es de {calidad_promedio:.2f}")
    print(f"La puntuación máxima de {c} es de {max_puntuacion}")"""

# Imprime una lista de todos los componentes y sus lotes, ordenados por puntuación de mayor a menor.
