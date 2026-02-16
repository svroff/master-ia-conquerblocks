
# ADMINISTRACION DE PROYECTOS:
# Eres un gerente de proyectos y necesitas un programa para administrar
# las tareas y responsabilidades de tu equipo.

# Cada tarea tiene un nombre, una descripción y un responsable asignado.

# Implementa un programa en Python que utilice un diccionario para almacenar 
# la información de las tareas.

# El programa debe permitir:
# 1. Agregar nuevas tareas.
# 2. Asignar responsables a las tareas existentes.
# 3. Actualizar las descripciones de las tareas.
# 4. Mostrar la lista completa de tareas y responsables.

# diccionario
pacs = {
}

# 1. Agregar nuevas tareas.
pacs['tarea_sql'] = {
    "descripcion_tarea" : "aplicar job sql",
    "responsable" : ""
}
pacs['tarea_fs'] = {
    "descripcion_tarea" : 'revisar filesystem E:',
    'responsable' : ""

}

# 2. Asignar responsables a las tareas existentes.
pacs['tarea_fs']['responsable'] = 'Sergi'
pacs['tarea_sql']['responsable'] = 'David'

# 3. Actualizar las descripciones de las tareas.
pacs['tarea_fs']['descripcion_tarea'] = 'revisar FS C:'
pacs['tarea_sql']['descripcion_tarea'] = 'restructurar columnas table Estudios'

# 4. Mostrar la lista completa de tareas y responsables.
print("\n--- INFORME DE PROYECTOS ---")

for clave, valor in pacs.items():
    # 1. Sacamos los datos limpios a variables temporales
    # 'clave' ya es el nombre de la tarea (ej: tarea_sql)
    # 'valor' es el diccionario de dentro
    
    el_responsable = valor['responsable']
    la_descripcion = valor['descripcion_tarea']
    
    # 2. Imprimimos bonito usando esas variables
    # \t es un tabulador para que quede alineado, o puedes usar guiones
    print(f"📌 TAREA: {clave}")
    print(f"   - Responsable: {el_responsable}")
    print(f"   - Detalle: {la_descripcion}")
    print("-" * 30) # Separador visual
