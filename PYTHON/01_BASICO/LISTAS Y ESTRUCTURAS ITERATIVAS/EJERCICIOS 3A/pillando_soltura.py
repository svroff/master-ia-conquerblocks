import numbers
mi_lista = ["sol", "luna", 3, -5, "mar", "sol", 8, "luna", -2, "tierra", 3]

# 1. Escribe un programa en Python para encontrar los elementos duplicados de una lista, añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los elementos únicos.
mi_segunda_lista = []
for n in mi_lista:
    if mi_lista.count(n) > 1 and n not in mi_segunda_lista:
        mi_segunda_lista.append(n)
        mi_lista.remove(n)
print(mi_segunda_lista)
print(mi_lista)
print('------------------------------------------')  
# 2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente. 
mi_tercera_lista = []
lista = [1,5,3,8,4,9,23,6,28]  
for n in mi_lista:
    if isinstance(n, numbers.Number): # separo los numeros de la lista original para tener una lista de numeros y otra de palabras. No puedo ordenar listas "híbridas"
        mi_tercera_lista.append(n)
        mi_lista.remove(n)
# quiero cambiar el nombre para que sea más claro. creo de nuevas usando copy() y elimino las antiguas con del
mi_lista_numeros = mi_tercera_lista.copy() 
mi_lista_palabras = mi_lista.copy()
del mi_lista
del mi_tercera_lista


lista = lista + mi_lista_numeros
lista.sort(reverse=True)
print(lista)
print('------------------------------------------')  

# 3. Escribe un script que encuentre el segundo número más grande de una lista. 
mi_lista_numeros.sort(reverse=True) # [8, 3, -2, -5]
# ahora tenemos una lista numérica ordenada de mayor a menor. Sabemos que la posición 0 es la mayor, entonces el segundo más grande es la posición 1.  

print(mi_lista_numeros[1]) 
print('------------------------------------------')  
# 4. Crea un script que cuente el número de elementos más grandes que un determinado número dado por el usuario (supón una lista numérica). 

# 5. Crea un script dado un número introducido por el usuario o determinado al inicio del programa, realice la suma de aquellos números que sean divisibles por este. 
# 6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto que es inferior al número introducido o determinado al inicio del programa. 
# 7. Crea un script que extraiga los elementos comunes entre dos listas. 
# 8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista (P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2) 
# 9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo números positivos de la lista original. 
# 10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de los strings de la lista original. 
# 11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en mayúscula. 