'''
NUMEROS PRIMOS 2: 

Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con 
los números primos de la lista original. Además, el script debe de volver el número total de 
números primos encontrados y la suma de los números primos encontrados

'''

# creamos las listas
lista_numeros = [3, 4, 5, 8, 11, 14, 17, 20, 23, 27, 29, 33, 37, 40]
lista_primos = []
# creamos el bucle para iterar la lista de numeros
for n in lista_numeros:
    for divisor in range(2, n): # usamos un bucle con for para pasarle todos los numeros entre 2 y n para que vaya diviendo entre todos y sepamos cual es primo o no.
        if n % divisor == 0:
            break # si encuentra un número que no es primo para
    else: # si lo encuentra y además no está ya préviamente en la lista de primos, lo añadimos con append()
        lista_primos.append(n)

print(f'La lista de números primos es la siguiente: {lista_primos}')
print(f'El número total de números primos encontrados es de {len(lista_primos)}') # usamos len() para contar
print(f'La suma total de todos los números primos es de: {sum(lista_primos)}') # usamos sum() para sumar 

 