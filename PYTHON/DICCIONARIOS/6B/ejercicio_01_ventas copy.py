# --- VERSIÓN 2: REGISTRO DE VENTAS (Lógica Acumulativa) ---

# 1. Empieza con el registro de ventas del día VACÍO (la tienda abre ahora).
ventas_diarias = {}

# 2. Primera venta de la mañana:
# Cliente 1 compra: 2 "Camisetas" y 1 "Pantalón".
# Como el diccionario está vacío, ASIGNAMOS (=) los valores directamente.
ventas_diarias["Camiseta"] = 2
ventas_diarias["Pantalón"] = 1

print(f"Ventas a media mañana: {ventas_diarias}")

# 3. Segunda venta (LA CLAVE DEL EJERCICIO):
# Cliente 2 compra: 3 "Camisetas" más.
# AQUÍ ESTÁ EL RETO: No uses =, usa += para sumar a lo que ya había.
# (Tu código aquí) ...
ventas_diarias["Camiseta"] += 3

# 4. Cálculo final:
# Usa .values() y sum() para decirme cuántos productos se han vendido en total hoy.
total_productos = sum(ventas_diarias.values())

print("--------------------------------")
print(f"Resumen final de ventas: {ventas_diarias}")
print(f"Total de ítems vendidos: {total_productos}")