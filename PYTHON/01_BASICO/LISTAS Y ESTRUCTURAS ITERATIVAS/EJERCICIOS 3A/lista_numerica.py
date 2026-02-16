# Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].
numeros = [1,2,3,4,5,6,7,8,9,10]

# Crea una lista llamada sólo con los pares y en orden inverso.
numeros_pares = []
for n in numeros:
    if n % 2 == 0:
        numeros_pares.append(n)
numeros_pares = numeros_pares[::-1]

# Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola.
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)

# Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
mas_pequeño = min(numeros)

# Haz lo mismo con el número más alto
mas_alto = max(numeros)

# Suma todos los elementos de la lista con y sin un bucle.
suma_total = sum(numeros)

suma_total_bucle = 0

for n in numeros:
    suma_total_bucle += n

# Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras el punto 2.
print(numeros.index(8))
print(numeros_pares.index(8))