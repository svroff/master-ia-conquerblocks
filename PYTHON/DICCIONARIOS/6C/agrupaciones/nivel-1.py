mascotas = ["perro", "gato", "pez", "canario", "hamster", "cobaya"]
zoo = {}
# Recorre la lista mascotas y agrúpalos en el diccionario zoo usando su primera letra como clave.
for mascota in mascotas:
    letra_inicial = mascota[0]

    if letra_inicial not in zoo:
        zoo[letra_inicial] = []

    zoo[letra_inicial].append(mascota)

for c in zoo:
    print(f"{c}: {zoo[c]}")
