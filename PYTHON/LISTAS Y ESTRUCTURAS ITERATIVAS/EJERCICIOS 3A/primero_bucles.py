'''
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una 
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el 
centro de la estructura. 
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
* 

'''

# Pedimos un numero entero por pantalla
valor = int(input('Dime un valor: '))

# Hacemos un bucle para imprimir la primera parte de la pirámide. Irá sumando hasta llegar al valor introducido.
for i in range(1, valor + 1):
    print("*" * i)

# y aquí tenemos que hacer la segunda parte de la pirámide que irá restando hasta el final.
for y in range(valor - 1, 0,  - 1):
    print("*" * y)