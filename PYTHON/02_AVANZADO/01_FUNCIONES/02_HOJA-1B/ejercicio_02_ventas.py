# ==========================================
# EJERCICIO 2: GESTIÓN DE VENTAS
# ==========================================

from webbrowser import get


print("\n--- EJERCICIO 2: VENTAS ---")

# 1. VARIABLE GLOBAL
# Crea una lista vacía llamada 'ventas' donde iremos guardando los datos.
# Tu código aquí:
ventas = []


# 2. FUNCIÓN DE REGISTRO
def agregar_venta(producto, precio):
    # Tienes que hacer 2 cosas aquí:
    # A) Crear un diccionario con las claves "Producto" y "Precio" usando los datos que te llegan.
    diccionario = {"Producto": producto, "Precio": precio}
    # B) Añadir ese diccionario dentro de la lista 'ventas' que creaste arriba.
    ventas.append(diccionario)


# 3. FUNCIÓN DE REPORTE
def mostrar_ventas():
    # Tienes que recorrer la lista 'ventas' (bucle for).
    # Por cada venta, imprime una frase bonita tipo: "Producto: Manzana | Precio: 0.50€"
    for v in ventas:
        print(f"Producto {v['Producto']} | Precio: {v['Precio']} ")


# --- ZONA DE PRUEBAS ---
# Cuando termines, descomenta estas líneas para ver si funciona:

agregar_venta("Café", 1.50)
agregar_venta("Donut", 2.00)
mostrar_ventas()
