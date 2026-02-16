
# REGISTRO DE ASISTENCIAS:
# Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
# estudiantes a lo largo del semestre.

# Cada estudiante tiene un nombre y una lista de fechas en las que asistió a clases.

# Implementa un programa en Python que utilice un diccionario para almacenar 
# la información de las asistencias.

# El programa debe permitir:
# 1. Registrar la asistencia de los estudiantes (Crear entrada con lista).
# 2. Agregar nuevas fechas de asistencia (Append a la lista existente).
# 3. Mostrar la lista de estudiantes y las fechas en las que asistieron.

# Pista: Construye un diccionario de listas -> { "Nombre": ["Fecha1", "Fecha2"] }

# --- TU CÓDIGO EMPIEZA AQUÍ ---
registro_alumnos = {}

# 1. Registrar la asistencia de los estudiantes (Crear entrada con lista).
registro_alumnos["Felipe"] = ['19/02/1995']
registro_alumnos["Ainoa"] = ['25/02/1998']
registro_alumnos["Sergi"] = ['13/11/1965']

# 2. Agregar nuevas fechas de asistencia (Append a la lista existente).
registro_alumnos["Felipe"].append('20/02/1995')
registro_alumnos["Felipe"].append('21/02/1995')
registro_alumnos["Sergi"].append('14/11/1965')

# 3. Mostrar la lista de estudiantes y las fechas en las que asistieron.
for clave, valor in registro_alumnos.items():
    print(f"ALUMNO: {clave}")
    for v in valor:
        print(f"    - Asistió el: {v}")

