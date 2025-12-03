# TRABAJANDO CON TUPLAS
import numpy as np

# Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea.
"""personajes = ("Luffy", "Naruto", "Ichigo")
for p in personajes:
    print(p)"""
# Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla. ¿Cuáles son las diferencias?
"""villanos = ["Barbanegra", "Madara", "Aizen"]
villanos[1] = "Pain"
print(villanos)"""
# 3. Crea una tupla de enteros y devuelve la suma de los elementos.
"""enteros = (12, 23, 54, 2, 6, 7, 213)
suma_enteros = sum(enteros)
print(suma_enteros)
print(type(suma_enteros))"""
# 4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string.
personajes = ("Luffy", "Naruto", "Ichigo")

# 5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares.
enteros = (12, 23, 54, 2, 6, 7, 213)
"""total = 1

for e in enteros:
    if e % 2 == 0:
        total = total * e

condicion_pares = np.array(enteros) % 2 == 0
total_np = np.prod(enteros)"""


# 6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente.

copia_array = np.array(enteros)
orden_descendiente = np.sort(copia_array)[::-1]

# 7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados.
enteros_ = (2, 2, 2, 2, 24, 5, 3, 6, 6, 6, 6, 7, 2, 8, 9)
set_enteros = set(enteros_)
copia_enteros = np.array(enteros_)
enteros_ordenados = np.unique(copia_enteros)

# 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario.
"""print(f"Dada la tupla {enteros_} elige un entero y te diré si se encuentra o no.")
valor_a_buscar = int(input("Elige: "))

print(valor_a_buscar in enteros_)"""

# 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.

# 10.  Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
# 11.  Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. (Prueba añadiendo key=len a las funciones max y min).
# 12.  Crea un script que dada una tupla devuelva el contenido en orden revertido.
# 13.  Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos elementos de la tupla interna correspondiente.
