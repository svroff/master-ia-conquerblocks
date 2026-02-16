'''
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año.
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos,etc.). 

Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en
cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3
columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de
NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.
'''

# importamos numpy
import numpy as np

# conjunto de datos de ventas de una tienda durante un año.
# Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la venta y la categoría de producto vendido

ventas = np.array([
    ('Enero', 100, 'ropa'),
    ('Enero', 200, 'alimentos'),
    ('Enero', 150, 'ropa'),
    ('Febrero', 120, 'alimentos'),
    ('Febrero', 180, 'electrónicos'),
    ('Febrero', 200, 'alimentos'),
    ('Febrero',  90, 'ropa'),
    ('Marzo', 110, 'electrónicos'),
    ('Marzo', 100, 'alimentos')
], dtype=[('fecha', 'U10'), ('monto', 'i4'), ('categoria', 'U12')])

print("Shape:", ventas.shape)
print("Monto total:", ventas['monto'].sum())
print("Ventas Enero:", ventas[ventas['fecha'] == 'Enero']['monto'].sum())
print("Ventas Febrero:", ventas[ventas['fecha'] == 'Febrero']['monto'].sum())
print("Ventas Marzo:", ventas[ventas['fecha'] == 'Marzo']['monto'].sum())



