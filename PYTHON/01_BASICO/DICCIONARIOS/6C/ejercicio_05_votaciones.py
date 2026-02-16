# ==========================================
# 🗳️ HOJA 6C (Parte 2): ANÁLISIS DE VOTACIONES
# ==========================================
# OBJETIVO:
# 1. Registrar votos (sumar a contadores).
# 2. Listar candidatos y votos.
# 3. Encontrar al GANADOR (el que más votos tiene).
# 4. Calcular el PORCENTAJE de votos de cada uno.

# Simulamos una base de datos de votos ya contados parcialmente
# Clave: Nombre del candidato
# Valor: Cantidad de votos actuales
resultados = {"Alicia": 150, "Benito": 450, "Carmen": 320, "David": 80}
print("-" * 50)
print("\n--- SISTEMA DE RECUENTO ELECTORAL ---")

# ---------------------------------------------------------
# MISIÓN 1: REGISTRAR NUEVOS VOTOS
# Llegan votos de última hora.
# Suma 50 votos a "Alicia" y 100 votos a "David".
# Imprime el diccionario actualizado.
# ---------------------------------------------------------
print("\n--- 1. ACTUALIZACIÓN DE VOTOS ---")
resultados["Alicia"] += 50
resultados["David"] += 100

print(resultados)

# ---------------------------------------------------------
# MISIÓN 2: LISTADO DE CANDIDATOS
# Imprime la lista de candidatos con sus votos actuales.
# Formato sugerido: "Candidato: [Nombre] | Votos: [Cantidad]"
# ---------------------------------------------------------
print("\n--- 2. RESULTADOS ACTUALES ---")
for c, v in resultados.items():
    print(f"{c} : {v}")

# ---------------------------------------------------------
# MISIÓN 3: EL GANADOR 🏆
# Debes encontrar quién tiene más votos.
# PISTA: Necesitas una variable para guardar el 'record' de votos
# y otra para guardar el nombre del ganador mientras recorres.
# ---------------------------------------------------------
print("\n--- 3. CANDIDATO GANADOR ---")

ganador = ""
max_votos = 0

# ... TU LÓGICA AQUÍ ...
# max_votos = max(resultados.values())

for nombre, votos in resultados.items():
    if votos > max_votos:
        max_votos = votos
        ganador = nombre

print(f"El ganador es {ganador} con {max_votos} votos.")


# ---------------------------------------------------------
# MISIÓN 4: PORCENTAJES 📊
# Calcula qué % del total representa cada candidato.
# PISTA 1: Primero necesitas sumar TODOS los votos (el 100%).
# PISTA 2: La fórmula es (Votos Candidato / Total) * 100
# ---------------------------------------------------------
print("\n--- 4. ESTADÍSTICAS DEL ESCRUTINIO ---")

total_votos = 0

# Paso A: Calcular el total de votos (suma de todos los valores)
# ... TU LÓGICA AQUÍ ...
total_votos = sum(resultados.values())

print(f"Total de votos emitidos: {total_votos}")
print("-" * 30)

# Paso B: Calcular y mostrar porcentajes
# ... TU LÓGICA AQUÍ ...
porcentajes = {}

for candidato, votos in resultados.items():
    formula = (votos / total_votos) * 100

    if candidato not in porcentajes:
        porcentajes[candidato] = formula

for c, v in porcentajes.items():
    print(f"Candidato: {c}: {v:.2f}%")
