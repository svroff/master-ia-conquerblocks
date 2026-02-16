# REGISTRO DE VENTAS:
# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias de tus productos.
# Cada producto tiene un nombre y una cantidad vendida.
# Implementa un programa en Python que utilice un diccionario para almacenar la información.
# El programa debe permitir:
# 1. Registrar ventas de productos (añadir o crear).
# 2. Actualizar la cantidad vendida de un producto existente (sumar).
# 3. Calcular el total de ventas diarias (sumar todos los valores).

# creamos el diccionario y añadimos ventas de productos.
# stock actual
tienda = {
    "ventas_videojuegos": {"ps5": 29, "pc": 18, "switch": 45},
    "ventas_peliculas": {"accion": 13, "drama": 29, "comedia": 59},
}
print(f"Abro la tienda con el siguiente stock: ")
for clave, valor in tienda.items():
    print(f"{clave} : {valor}")

print("-------------------------------------------------------------------------------")
# supongamos que hemos vendido 2 juegos de ps5, 9 de switch y 1 película de drama.
# primero me guardo el stock antes de abrir la tienda
total_stock_pre_ventas_videojuegos = sum(tienda.get("ventas_videojuegos").values())
total_stock_pre_ventas_peliculas = sum(tienda.get("ventas_peliculas").values())
total_stock_pre_ventas = (
    total_stock_pre_ventas_peliculas + total_stock_pre_ventas_videojuegos
)

# creo unas ventas 'hardcoded'
print("Cierro la tienda con el siguiente stock: ")
tienda.get("ventas_videojuegos")["ps5"] -= 2
tienda.get("ventas_videojuegos")["switch"] -= 9
tienda.get("ventas_peliculas")["drama"] -= 1

for clave, valor in tienda.items():
    print(f"{clave} : {valor}")

print("-------------------------------------------------------------------------------")

# calculamos el total de ítems después de las ventas.

total_stock_post_ventas_videojuegos = sum(tienda.get("ventas_videojuegos").values())
total_stock_post_ventas_peliculas = sum(tienda.get("ventas_peliculas").values())
total_stock_post_ventas = (
    total_stock_post_ventas_peliculas + total_stock_post_ventas_videojuegos
)


print(f"El stock al abrir la tienda es de {total_stock_pre_ventas} items en la tienda")

print(f"El stock a final del día es de: {total_stock_post_ventas} items en la tienda")
