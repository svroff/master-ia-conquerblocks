'''
BOT DE TRADING:
Un bot de trading está programado para realizar ciertas acciones con respecto a un producto 
financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del 
producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está 
entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está 
estrictamente por encima de 150 el bot deberá imprimir la orden de vender.
'''

# definimos los precios del producto para comparar
precio_compra = 100
precio_venta = 151

# pedimoss el precio por pantalla
precio = int(input('Dime el precio actual: '))

# comparamos
if (precio >= precio_compra and precio < precio_venta):
    print('Holdea')
elif (precio < precio_compra):
    print('Compra')
elif(precio > precio_venta):
    print('Vende')