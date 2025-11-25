'''
Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un 
programa para realizar un seguimiento de los productos que has vendido y el valor total de las 
ventas. Supongamos que hay un total de 10 productos.  

Tú has vendido 5 de estos productos en las siguientes cantidades: 

Producto 1:     3 unidades 
Producto 2:     1 unidad 
Producto 5:     7 unidades 
Producto 6:     2 unidades 
Producto 9 :    4 unidades 

Los precios de cada uno de estos productos son como siguen: 

Producto 1: 30.0 EU      
Producto 2: 9.8 EU      
Producto 3: 42.5 EU      
Producto 4: 32.6 EU      
Producto 5: 71.5 EU      
Producto 6: 44.0 EU
Producto 7: 21.2 EU  
Producto 8: 53.2 EU
Producto 9: 25.3 EU
Producto 10: 57.8 EU

Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima 
la cantidad total de ventas, el dinero facturado por producto y el dinero total.  
'''


# creamos las listas
precio_productos=[30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.3, 25.3, 57.8]
unidades_vendidas=[3, 1, 0, 0, 7, 2, 0, 0, 4, 0]

# creamos variables

cantidad_total_ventas = sum(unidades_vendidas)
precio_por_producto = 0
dinero_facturado_por_producto = []
dinero_total = 0

# buscamos los precios por producto multiplicando cada valor de cada indice con su correspondiente en la otra lista.
# es importante que esten ordenados.

for p in range(0, len(precio_productos)):
    precio_por_producto = precio_productos[p] * unidades_vendidas[p]
    dinero_facturado_por_producto.append(precio_por_producto)

dinero_total = sum(dinero_facturado_por_producto)  

# imprimimos por pantalla

print(f'Cantidad total de ventas: {cantidad_total_ventas} unidades vendidas')
print(f'El dinero facturado por producto es: {dinero_facturado_por_producto}')
print(f'Y el dinero total ha sido: {dinero_total} Euros')