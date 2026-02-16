'''

SCRABBLE: 

Supongamos una lista de caracteres llamada “palabras“ que representa una mano de 
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el 
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la 
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos 
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano. 

'''
# lista de palabras 
palabras = ["A5", "B3", "C2", "D4"]
# creamos una variable donde guardaremos los puntos
total_puntos = 0
# bucle para leer cada ficha
for ficha in palabras:
    puntos = int(ficha[1]) # debemos de indicarle a la variable ficha que sea un entero y que es la segunda posición de cada iteración ( A y 5)
    total_puntos += puntos # acumulamos el valor sumándolo a total_puntos

print(total_puntos)
