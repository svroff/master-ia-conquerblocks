# Crea un array_1 lleno ceros con una longitud de 8 elementos.
import numpy as np

'''array_1 = np.arange(1,9, dtype =  np.int8)'''

# Haz que todos los elementos de este array sean igual a 2
'''array_1.fill(2)

# Crea un array_2 que contenga todos los números pares del 1 al 10.
array_2 = np.arange(2,11,2, dtype =  np.int8)'''

# Suma todos los elementos del array_2 usando un bucle y después usando un método de numpy. Compara los resultados
'''suma_array_2 = 0
for i in array_2:
    suma_array_2 += i'''
    
'''print(suma_array_2) # mismo resultado 30
print(array_2.sum()) # mismo resultado 30'''

# Revierte array_2 y guárdalo en una variable independiente.

'''array_2_revertido = array_2[::-1]'''

# Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido
# (Pista: Investiga el uso de intersect1d() de numpy)    

'''elementos_comunes_1 = np.intersect1d(array_1, array_2)
elementos_comunes_2 = np.intersect1d(array_2, array_2_revertido)'''

# Crea un arrays lleno de 1s con una longitud dada por el usuario
'''
longitud = int(input('Dime la longitud del array:  '))
array_usuario = np.arange(1, longitud+1, dtype=np.int8)
array_usuario.fill(1)

print(array_usuario)
'''

# Crea un array con 15 números enteros aleatorios entre 1 y 100
'''rng = np.random.default_rng()
a_15 = rng.integers(1, 101, size=15)'''

# Multiplica todos los elementos del array usando un bucle y después usando un método de numpy. Compara los resultados
'''mult_total = 1
for i in a_15:
    mult_total *= i

mult_total_np = a_15.prod()'''

# Crea otro array con 15 números decimales aleatorios entre 0 y 1
'''b_15 = rng.random(15)'''


# Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un operador y después con una función de numpy
'''c_15 = a_15 + b_15
c = np.add(a_15, b_15)'''

# Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
'''c_15_resta = a_15 - b_15
c_15_resta_funcion_np = np.subtract(a_15, b_15)'''

# Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy
'''m = a_15 * b_15
m2 = np.multiply(a_15, b_15)'''

# Encuentra el valor más alto del primer array que has creado.
'''indice_mas_alto = a_15.argmax()
print(a_15[indice_mas_alto])'''

# Calcula la media (mean), la mediana (median) y la deviación estandar (standard deviation) de los arrays (Nota: No nos importa el significado matemático de estos valores, lo importante es que encuentres que función de numpy necesitas. Puedes hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele haber más resultados).
'''rng = np.random.default_rng()
arr = rng.integers(1, 101, size=10)

media = arr.mean() # la media
mediana = np.median(arr) # la mediana
deviacion = np.std(arr) # deviacion estandar

print(f"Media     : {arr.mean():.2f}")
print(f"Mediana   : {np.median(arr):.2f}")
print(f"Desv. Est.: {np.std(arr, ddof=0):.2f}")'''

# Crea un arrays lleno de 1s con una longitud dada por el usuario
# Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)

'''filas = int(input('Dime las filas para el array  '))
columnas = int(input('Dime las columnas del array  '))

arr = np.eye(filas, columnas, dtype=int)
arr.fill(1)

 print(arr)'''

# 11.Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)

'''arr2 = np.identity(filas, dtype=int)
 print(arr2)'''

# 12.Concatena ambas estructuras horizontalmente y verticalmente
'''arr2.fill(2)
arr3_1 = np.concatenate((arr, arr2), axis = 0)
arr3_2 = np.concatenate((arr, arr2), axis = 1)
print(arr3_1)
print('------------------------')
print(arr3_2)'''