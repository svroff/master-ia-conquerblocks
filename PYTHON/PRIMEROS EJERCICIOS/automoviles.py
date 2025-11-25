'''
Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.

'''



numero_serie1 = int(input('Cuántos serie 1 has vendido?: '))
numero_plus = int(input('Cuántos serie plus has vendido?: '))
numero_todoterreno = int(input('Cuántos todoterreno has vendido?: '))

serie_1_comision = numero_serie1 * 20000 * 0.03
serie_plus_comision = numero_plus * 35000 * 0.05
serie_todoterreno_comision = numero_todoterreno * 60000 * 0.07

comisiones_totales = serie_1_comision + serie_plus_comision + serie_todoterreno_comision

print('Has vendido un total de ', numero_serie1, ' series 1 y eso es una comision de ', serie_1_comision, ' euros')
print('Has vendido un total de ', numero_plus, ' series plus y eso es una comision de ', serie_plus_comision, ' euros')
print('Has vendido un total de ', numero_todoterreno, ' series todoterreno y eso es una comision de ', serie_todoterreno_comision, ' euros')
print('Un total de ', comisiones_totales, ' euros en comisiones')
