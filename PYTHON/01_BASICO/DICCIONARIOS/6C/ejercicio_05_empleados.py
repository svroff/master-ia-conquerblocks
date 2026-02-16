# ==========================================
# 📄 HOJA 6C: GESTIÓN DE EMPLEADOS (DICCIONARIOS ANIDADOS)
# ==========================================
# OBJETIVO:
# Trabajar con un diccionario que contiene otros diccionarios (base de datos).
# Realizar consultas, actualizaciones y cálculos de agrupación.

# Base de datos de empleados
# Clave: ID del empleado (Entero)
# Valor: Diccionario con sus datos personales
empleados = {
    101: {"nombre": "Ana", "edad": 30, "departamento": "Ventas", "salario": 3000},
    102: {"nombre": "Luis", "edad": 25, "departamento": "IT", "salario": 4000},
    103: {"nombre": "Carlos", "edad": 40, "departamento": "Ventas", "salario": 3500},
    104: {"nombre": "Maria", "edad": 35, "departamento": "IT", "salario": 4200},
    105: {"nombre": "Sofia", "edad": 28, "departamento": "RRHH", "salario": 2800},
}
print("-" * 50)

print("\n--- INICIO DEL PROGRAMA ---")

# ---------------------------------------------------------
# MISIÓN 1: CONSULTA BÁSICA
# Recorre el diccionario e imprime:
# "ID: [id] | Nombre: [nombre] | Dept: [departamento]"
# ---------------------------------------------------------
print("\n--- 1. LISTADO DE EMPLEADOS ---")
for clave, valor in empleados.items():
    print(f'ID: {clave} | Nombre: {valor["nombre"]} | Dept: {valor["departamento"]}')

# ---------------------------------------------------------
# MISIÓN 2: ACTUALIZACIÓN SALARIAL
# Sube el sueldo de 'Carlos' (ID 103) a 3800.
# Imprime su nuevo salario para confirmar.
# ---------------------------------------------------------
print("\n--- 2. ACTUALIZACIÓN DE SUELDO ---")
empleados[103]["salario"] = 3800
print(
    f'ID: {list(empleados.keys())[2]} | Nombre: {empleados[103]["nombre"]} | Nuevo salario: {empleados[103]["salario"]}'
)

# ---------------------------------------------------------
# MISIÓN 3: CONTRATACIÓN (AÑADIR)
# Añade un nuevo empleado con ID 106:
# Nombre: "Jorge", Edad: 22, Dept: "Ventas", Salario: 2500
# ---------------------------------------------------------
print("\n--- 3. CONTRATACIÓN DE JORGE ---")
empleados[106] = {
    "nombre": "Jorge",
    "edad": 22,
    "departamento": "Ventas",
    "salario": 2500,
}
for clave, valor in empleados.items():
    print(f'ID: {clave} | Nombre: {valor["nombre"]} | Dept: {valor["departamento"]}')
# ---------------------------------------------------------
# MISIÓN 4: ANÁLISIS DE DATOS (AGRUPACIÓN) ⚠️ EL RETO DE HOY
# Calcula el SALARIO PROMEDIO por departamento.
# Pista: Primero necesitas agrupar los sueldos en listas:
# { 'Ventas': [3000, 3800, 2500], 'IT': ... }
# ---------------------------------------------------------
print("\n--- 4. SALARIOS POR DEPARTAMENTO ---")

sueldos_por_depto = {}

# ... TÚ CÓDIGO AQUÍ ...
for e in empleados:
    dept = empleados[e]["departamento"]
    sueldo = empleados[e]["salario"]

    if dept not in sueldos_por_depto:
        sueldos_por_depto[dept] = []

    sueldos_por_depto[dept].append(sueldo)

print("\n--- PROMEDIO SALARIAL POR DEPARTAMENTO ---")
for depto, lista_sueldos in sueldos_por_depto.items():
    # 1. Calcular promedio (Suma / Cantidad)
    promedio = sum(lista_sueldos) / len(lista_sueldos)

    # 2. Imprimir bonito
    print(f"Departamento: {depto} | Sueldo Medio: {promedio}€")
print("\n")
print("-" * 50)
