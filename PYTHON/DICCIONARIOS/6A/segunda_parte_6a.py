# --- LISTAS DE DICCIONARIOS ---

# 18. Crea una lista llamada "estudiantes" que contenga dos diccionarios.
# Cada diccionario representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos valores.


estudiantes = {
    "primer_alumno" : {
        "nombre" : "Sergi",
        "edad" : 31
    },
    "segundo_alumno" : {
        "nombre" : "Andreia",
        "edad" : 29
    }
}
# 19. Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las mismas claves "nombre" y "edad".
estudiantes["tercer_alumno"] = {
    "nombre" : "Adri",
    "edad" : 28
}

# 20. Elimina el segundo estudiante de la lista "estudiantes". 
estudiantes.pop("segundo_alumno")

# 21. Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor.
estudiantes.get("primer_alumno")["edad"] = 34

print(estudiantes)
print("------------------------------------------------------")

# --- ANIDAMIENTO DE DICCIONARIOS ---

# 22. Crea un diccionario llamado "productos" que contenga dos entradas.
# Cada entrada representa un producto y tiene a su vez las claves "nombre" y "precio" con sus respectivos valores.

productos = {
    "primer_producto" : {
        "nombre" : "tomates",
        "precio" : 15
    },
    "segundo_producto" : {
        "nombre" : "platanos",
        "precio" : 12
    }
}

for clave, valor in productos.items():
    nombre_producto = valor["nombre"]
    precio_producto = valor["precio"]
    
    print(f"El producto {nombre_producto} cuesta {precio_producto} euros")
    
print("------------------------------------------------------")

# 23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y valor.
productos["tercer_producto"] = {
    "nombre" : "pintalabios",
    "precio" : 18
}

for clave, valor in productos.items():
    nombre_producto = valor["nombre"]
    precio_producto = valor["precio"]
    
    print(f"El producto {nombre_producto} cuesta {precio_producto} euros")
print("------------------------------------------------------")

# 24. Crea un diccionario llamado "equipos" que contenga tres entradas.
# Cada entrada representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus respectivos valores.
# Los valores de "jugadores" deben ser listas con los nombres de los jugadores.

equipos = {
    "entrada1" : {
        "nombre" : "Sistemas",
        "jugadores" : ["Carles", "Sisku", "Martin"]
    },
    "entrada2" : {
         "nombre" : "CPD",
        "jugadores" : ["Alejandro", "Pau", "Tamayo"]
    },
    "entrada3" : {
         "nombre" : "PACS",
        "jugadores" : ["Maribel", "David" , "Sergi"]
    }
}

for clave, valor in equipos.items():
    nombre_producto = valor["nombre"]
    precio_producto = valor["jugadores"]
    
    print(f"El equipo {nombre_producto} tiene a {precio_producto} ")

print("------------------------------------------------------")

# 25. Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor.
# La lista de jugadores debe contener al menos tres nombres. 
equipos["entrada4"] = {
    "nombre" : "SAP",
    "jugadores" : ["Sara", "Carlota", "Dani"]
}


for clave, valor in equipos.items():
    nombre_producto = valor["nombre"]
    precio_producto = valor["jugadores"]
    
    print(f"El equipo {nombre_producto} tiene a {precio_producto} ")
print("------------------------------------------------------")

# 26. Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario "equipos".
# Agrega un nuevo jugador a la lista. 

equipos.get("entrada4")["jugadores"].append("Ricard")

for clave, valor in equipos.items():
    nombre_producto = valor["nombre"]
    precio_producto = valor["jugadores"]
    
    print(f"El equipo {nombre_producto} tiene a {precio_producto} ")
print("------------------------------------------------------")