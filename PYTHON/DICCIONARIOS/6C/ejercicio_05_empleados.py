# [cite: 4-7]
# GESTIÓN DE EMPLEADOS:
# Imagina que eres el gerente de recursos humanos de una empresa y
# necesitas gestionar la información de los empleados.

# Cada empleado tiene un nombre, salario y departamento al que pertenece.

# Implementa un programa en Python que permita:
# 1. Agregar nuevos empleados (Diccionario anidado).
# 2. Actualizar el salario de un empleado existente.
# 3. Mostrar la lista completa de empleados.
# 4. Calcular el promedio salarial por departamento.

# --- TU CÓDIGO EMPIEZA AQUÍ ---
# Diccionario con 3 empleados
empleados = {
    "emp_01": {"nombre": "Sergi", "salario": 1500, "dept": "PACS"},
    "emp_02": {"nombre": "David", "salario": 2500, "dept": "PACS"},
    "emp_03": {"nombre": "Maribel", "salario": 2800, "dept": "CDI-SAP"},
}
# 1. Agregar nuevos empleados (Diccionario anidado).
empleados["emp_04"] = {"nombre": "Alejandro", "salario": 1300, "dept": "CPD"}

# 2. Actualizar el salario de un empleado existente.
empleados["emp_01"]["salario"] = 1800

# 3. Mostrar la lista completa de empleados.
print("*" * 15)
print("LISTA DE EMPLEADOS")
print("*" * 15)
for clave, valor in empleados.items():
    print("-" * 20)
    print(f"Empleado: {clave}")
    for v in valor:
        print(f"{v}:    {valor[v]}")


# --- PASO 4: CALCULAR PROMEDIO POR DEPARTAMENTO ---

# 1. Crear un diccionario auxiliar (la mesa con los sobres vacíos)
# La clave será el departamento y el valor será una LISTA de sueldos.
sueldos_por_depto = {}

print("\n--- PROCESANDO SALARIOS ---")

for id_emp, datos in empleados.items():
    depto_actual = datos["dept"]
    sueldo_actual = datos["salario"]

    # LA MAGIA: Preguntamos si el sobre ya existe
    if depto_actual not in sueldos_por_depto:
        # Si es la primera vez que vemos este depto, creamos la lista vacía
        sueldos_por_depto[depto_actual] = []

    # Ahora que seguro que existe la lista, añadimos el sueldo
    sueldos_por_depto[depto_actual].append(sueldo_actual)

# 2. Ahora que ya tenemos los sueldos agrupados, calculamos promedios
print("\n--- RESULTADOS ---")
for depto, lista_sueldos in sueldos_por_depto.items():
    promedio = sum(lista_sueldos) / len(lista_sueldos)
    print(f"Departamento: {depto} | Promedio: {promedio}€")
