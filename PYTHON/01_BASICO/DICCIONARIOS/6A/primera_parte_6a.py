# --- TRABAJANDO CON DICCIONARIOS ---

# 1. Crea un diccionario vacío llamado "mi_diccionario"[cite: 6].
mi_diccionario = {}
# print(type(mi_diccionario))

# 2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor sea tu nombre[cite: 7].
mi_diccionario["nombre"] = 'Sergi'

# 3. Accede e imprime el valor asociado con la clave "nombre" en "mi_diccionario"[cite: 8].
print(mi_diccionario["nombre"])

# 4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False" en caso contrario[cite: 9].
if "edad" in mi_diccionario:
    print("True")
else:
    print("False")
# 5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor: "nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia favorita[cite: 10, 11].
estudiante = {
    "nombre" : "David",
    "edad" : 43,
    "materia" : "PACS"
}
# 6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad actual de tu amigo[cite: 12].
estudiante["edad"] = 42
# 7. Elimina el par clave-valor con la clave "materia" del diccionario "estudiante"[cite: 13].
estudiante.pop("materia")
# 8. Imprime todas las claves en el diccionario "estudiante"[cite: 14].
print(estudiante.keys())
# --- LA AGENDA ---

# 9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor "1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor "5555555555"[cite: 15].
agenda = {
    "Juan" : "1234567890",
    "Joana" : "9876543210",
    "Jimena" : "5555555555"
}

# 10. Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor "9998887777"[cite: 16].
agenda["Julio"] = "9998887777"

# 11. Imprime el número de entradas (pares clave-valor) en el diccionario "agenda"[cite: 17].
print(len(agenda))

# 12. Crea una lista llamada "claves" que contenga todas las claves del diccionario "agenda"[cite: 18].
claves = list(agenda)

# 13. Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y "False" en caso contrario[cite: 19].
if "Juan" in agenda:
    print("True")
else:
    print("False")

# 14. Elimina la entrada con la clave "Jimena"[cite: 20].
agenda.pop("Jimena")
print(len(agenda))

# 15. Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e imprime cada par clave-valor en el formato "Nombre: Número"[cite: 21].
for clave, valor in agenda.items():
    print(f'{clave} : {valor}')

# 16. Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada"[cite: 22, 23].
print(agenda.get("Juan", "Clave no encontrada"))
# 17. Borra todas las entradas del diccionario "agenda"[cite: 24].
agenda.clear()
