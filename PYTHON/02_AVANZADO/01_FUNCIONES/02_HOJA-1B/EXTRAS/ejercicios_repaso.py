import random
import string

# ==========================================
# RETO 1: EL SORTEO JUSTO
# ==========================================
# Escribe una función llamada 'elegir_ganador' que reciba un texto con
# varios nombres separados por comas.
# La función debe convertir ese texto en una lista (investiga el método .split())
# y usar random.choice() para devolver el nombre del ganador.

print("\n--- RETO 1 ---")


# Tu código aquí:
def elegir_ganador(frase):
    frase_separada = frase.split(",")
    return random.choice(frase_separada)


frase_ejemplo = "sergi,alejandro,toni,david,maribel"
primer_reto = elegir_ganador(frase_ejemplo)
print(primer_reto)


# ==========================================
# RETO 2: EL GENERADOR DE NICKNAMES (GAMER TAGS)
# ==========================================
# Crea una función llamada 'generar_nickname' que reciba dos parámetros:
# un nombre y un adjetivo.
# La función debe juntarlos y añadir exactamente 3 números aleatorios al final.
# Ejemplo: generar_nickname("Gato", "Ninja") -> "GatoNinja482"

print("\n--- RETO 2 ---")


# Tu código aquí:
def generar_nickname(nombre, adjetivo):
    digits = string.digits
    nickname = (
        nombre
        + adjetivo
        + random.choice(digits)
        + random.choice(digits)
        + random.choice(digits)
    )
    return nickname


segundo_reto = generar_nickname("Lady", "Ratnik")
print(segundo_reto)

# ==========================================
# RETO 3: EL LANZADOR DE DADOS DE ROL (NIVEL JEFE)
# ==========================================
# Crea una función llamada 'lanzar_dados' que reciba dos parámetros:
# 1. cantidad_dados (cuántos dados tiramos, ej: 3)
# 2. caras (de cuántas caras es cada dado, ej: 6)
#
# La función debe simular tirar esos dados, sumar los resultados
# y devolver el total.
# (Pista: Necesitarás un bucle 'for' y usar random.randint(1, caras))

print("\n--- RETO 3 ---")


# Tu código aquí:
def lanzar_dados(cantidad_dados=3, caras=6):
    
