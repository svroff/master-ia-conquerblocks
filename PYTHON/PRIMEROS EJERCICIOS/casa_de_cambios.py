'''
Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)

La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario. 
'''

euros = float(input('¿Cuánto dinero tienes? '))
tasas_de_gestion = euros * 0.10
dolares = (euros - tasas_de_gestion) * 1.07
print("La casa se queda con el 10% que es " + str(tasas_de_gestion) + " euros")
print('Tienes ' + str(dolares) + ' en dólares')