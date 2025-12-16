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

"""copia_array = np.array(enteros)
orden_descendiente = np.sort(copia_array)[::-1]"""

# 7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados.
enteros_ = (2, 2, 2, 2, 24, 5, 3, 6, 6, 6, 6, 7, 1, 2, 8, 9)
set_enteros = set(enteros_)
copia_enteros = np.array(enteros_)
enteros_ordenados = np.unique(copia_enteros)

# 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla y falso en el caso contrario.
"""print(f"Dada la tupla {enteros_} elige un entero y te diré si se encuentra o no.")
valor_a_buscar = int(input("Elige: "))

print(valor_a_buscar in enteros_)"""

# 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas.
doble_tupla = enteros + enteros_

# 10.  Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
doble_tupla_arr = np.array(doble_tupla)


"""print(
    f"El valor máximo es: {doble_tupla_arr.max()} y el mínimo es: {doble_tupla_arr.min()}"
)"""
# 11.  Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. (Prueba añadiendo key=len a las funciones max y min).
heroes_marvel = (
    "Iron Man",
    "Thor",
    "Hulk",
    "Spider-Man",
    "Black Widow",
    "Doctor Strange",
    "Scarlet Witch",
    "Captain America",
)

"""print(max(heroes_marvel, key=len))
print(min(heroes_marvel, key=len))"""
# 12.  Crea un script que dada una tupla devuelva el contenido en orden revertido.

"""hm_orden_revertido = heroes_marvel[::-1]"""

# 13.  Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos elementos de la tupla interna correspondiente.
"""tupla_de_tuplas = ((10, 5), (20, 30), (7, 7), (100, -50))

suma_tuplas = np.array(tupla_de_tuplas).sum(axis=1)

s = 0
resultados = []
for t in tupla_de_tuplas:
    s = 0
    for tm in t:
        s = tm + s

    resultados.append(s)

sum_tuplas = tuple(resultados)

# ¿Serías capaz de escribir el código para ordenar la lista (usando sorted(lista, key=...)) basándote en quién ha encontrado más bugs? (Pista: usa lambda).
hackers = [("Neo", 10, 5), ("Trinity", 9, 50), ("Morpheus", 8, 20)]
hackers_ordenados = sorted(hackers, key=lambda x: x[2], reverse=True)
print(hackers_ordenados)"""

# 14. Crea un set y elimina uno de sus elementos.
mi_set = {"Andrea", "Sergio", 192, True}
mi_set.discard(192)

# 15. Crea un set vacío.
mi_set_vacio = set()
# 16. Crea dos sets y encuentra su union, su intersección y su diferencia.
primer_set = {"mimi", "titi", "sisi", "neo", "andreia", "hela"}
segundo_set = {"ares", "daira", "yaki", "mishi", "hela"}

union = set.union(primer_set, segundo_set)
inter = set.intersection(primer_set, segundo_set)
difer = set.difference(segundo_set, primer_set)

# 17. Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos.
interseccion = primer_set & segundo_set

# 18. Crea un script que dado un set con números devuelva el numero máximo y mínimo.
set_a = {15, 8, 92, 4, 15}
max(set_a)
min(set_a)

# 19. Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets.
set_c = primer_set ^ segundo_set

# 20. Crea un set con colores y comprueba si cierto color se encuentra en el set.
colores = {"rojo", "azul", "verde", "amarillo", "rojo"}
"""color = input("Di un color: ")

if color in colores:
    print(f"El set contiene el color: {color}")
else:
    print(f"No está el color: {color}")"""

# 21. Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo.

diff = primer_set - segundo_set

# 22. Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set.
set_a = {15, 8, 92, 4, 15}
list_set = list(set_a)
arr_list_set = np.array(list_set)
print(arr_list_set.prod())
