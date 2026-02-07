# REGISTRO DE PUNTAJES:
# Implementa un programa en Python que permita registrar y mantener un
# seguimiento de los puntajes de un juego.

# El programa debe permitir a los jugadores:
# 1. Registrar nombres y puntajes (Diccionario simple: { "Nombre": Puntos }).
# 2. Mostrar el puntaje más alto (max).
# 3. Mostrar el promedio de puntajes (sum / len).
# 4. Mostrar la cantidad total de jugadores (len).

# --- TU CÓDIGO EMPIEZA AQUÍ ---

# 1. Crea el diccionario con 3 o 4 jugadores y sus puntuaciones (Hardcoded)
puntos = {"Juan": 192, "Claus": 187, "Lorena": 199, "Sara": 176}

# 2. Calcula el puntaje más alto (Usa max() sobre los valores)
max_puntos = max(puntos.values())

# 3. Calcula el promedio (Suma total / Cantidad de jugadores)
suma_total = sum(puntos.values())
cantidad_jugadores = len(puntos)
promedio = suma_total / cantidad_jugadores

# 4. Mostrar la cantidad total de jugadores (len).
# 4. Imprime el reporte completo'''
print("\n")
print(f"El puntaje más alto lo tiene es de {max_puntos}")
print("-" * 30)
print(f"El promedio es de {promedio}")
print("-" * 30)
print(f"La cantidad total es de {cantidad_jugadores} jugadores")
