import numpy as np
'''
fdsfsdfsd
'''

a = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype = np.int8)
print(a.shape) # ver cuantas filas y columnas tiene
print(a.ndim) # ver cuantas dimensiones tiene

a_2 = a.reshape((9,1)) # modifica las filas y las columnas
print(a_2)
a_3 = np.arange(1,6,0.5)#crea un array uni que va del 1 al 6 de 0.5 en 0.5
print(a_3)
print(type(a_3))
# por defecto un np array es float.
eye_array = np.eye(3,3,dtype=int) # crea un array bi de 3 filas y 3 columnas en int
eye_array[eye_array == 0] = 6 # los valores que son 0 ahora son 6
eye_array += 2 # suma +2 a todos los valores
eye_array.fill(5) # convierte todo en 5
print('------------------------')
print(eye_array)
print(eye_array.sum())# sumamos todos los valores
print(eye_array.sum(axis=1))# sumamos las filas
print(eye_array.sum(axis=0))# sumamos las columnas
prod_array = eye_array.prod()# multiplicamos todo
prod_array = eye_array.prod(axis=1)# multiplicamos las filas
prod_array = eye_array.prod(axis=0)# multiplicamos las columnas
print('------------------------')
print(eye_array.mean()) # media de todos los valores
print(eye_array.max()) # máximo de todos los valores
print(eye_array.min()) # mínimo de todos los valores
print(eye_array.argmin()) # índice del valor mínimo
print(eye_array.argmax()) # índice del valor máximo
print('------------------------')
# primera forma para aplanar un array como si fuese una lista
b = np.arange(1,10).reshape((3,3))
array_plano = b.reshape(b.size)
print(b)
print(array_plano)
print('------------------------')
# método principal para hacerlo
array_plano = b.flatten()
print(b)
print(array_plano)
print('------------------------')
# .ravel() esta copia no es independiente, es como view y copy.
array_plano = b.ravel()
print(b)
print(array_plano)
print('------------------------')
# modifica los ejes de los valores (cambia las filas por las columnas)
array_transp = np.swapaxes(b,0,1) # le pasas el array, la fila y la columna ( el eje )
print(b)
print(array_transp)
print('------------------------')
array_transp = b.transpose (1,0)
print(b)
print(array_transp)


