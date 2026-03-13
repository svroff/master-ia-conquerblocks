# ==========================================
# ⚡ PRÁCTICA DE ARGUMENTOS ARBITRARIOS (*args y **kwargs)
# ==========================================

print("\n--- 1. EL PEDIDO DE PIZZA (*ARGS) ---")
# OBJETIVO: Crear una función que acepte CUALQUIER cantidad de ingredientes.
# Los *args se convierten en una TUPLA.


def hacer_pizza(tamaño, *ingredientes):
    print(f"\nPreparando pizza de {tamaño}cm con {len(ingredientes)} ingredientes:")

    # Truco: Imprimimos el TIPO de dato para ver qué es 'ingredientes'
    print(f"(Dato técnico: 'ingredientes' es del tipo {type(ingredientes)})")

    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


# PRUEBAS:
# Nota cómo pasamos argumentos sueltos y Python los empaqueta.
hacer_pizza(30, "Pepperoni")
hacer_pizza(45, "Queso", "Champiñones", "Piña", "Jamón")  # ¡Tantos como quieras!


print("\n\n--- 2. PERFIL DE USUARIO (**KWARGS) ---")
# OBJETIVO: Crear una función que acepte datos variables de un usuario.
# Los **kwargs se convierten en un DICCIONARIO.


def construir_perfil(nombre, apellido, **datos_extra):
    print(f"\nCreando perfil para: {nombre} {apellido}")

    # Truco: Vemos qué tipo de dato es 'datos_extra'
    print(f"(Dato técnico: 'datos_extra' es del tipo {type(datos_extra)})")

    # Como es un diccionario, usamos .items() para recorrerlo
    for clave, valor in datos_extra.items():
        print(f"  > {clave}: {valor}")


# PRUEBAS:
# Pasamos claves y valores que NO estaban definidos arriba.
construir_perfil("Sergi", "García", ciudad="Barcelona", curso="IA", nivel="Dios")
construir_perfil("Elon", "Musk", empresa="Tesla", red_social="X")


print("\n\n--- 3. LA SÚPER FUNCIÓN (MEZCLA) ---")
# OBJETIVO: Mezclar argumentos normales, *args y **kwargs.
# ORDEN OBLIGATORIO: (normales, *args, **kwargs)


def super_funcion(nombre, *numeros, **configuracion):
    print(f"\nEjecutando {nombre}...")
    print(f"Suma de números (*args): {sum(numeros)}")
    if "modo" in configuracion:
        print(f"Modo de ejecución (**kwargs): {configuracion['modo']}")


super_funcion("CalculadoraIA", 10, 20, 30, modo="Turbo", GPU=True)
