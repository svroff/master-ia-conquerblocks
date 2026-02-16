# ==========================================
# 📄 HOJA DE EJERCICIOS 1A: FUNCIONES
# ==========================================
# OBJETIVO:
# Familiarizarse con la sintaxis básica, parámetros, argumentos,
# retornos y valores por defecto.

print("\n--- INICIO DE LA PRÁCTICA ---")

# ---------------------------------------------------------
# EJERCICIO 1: EL SALUDO
# Define una función llamada "saludar" que tome un parámetro "nombre"
# y muestre un saludo personalizado.
# ---------------------------------------------------------
print("\n--- EJERCICIO 1 ---")


# Tu código aquí:
def saludar(nombre):
    print(f"Hola {nombre} un placer saludarte")


saludar("Sergi")

# ---------------------------------------------------------
# EJERCICIO 2: SUMA SIMPLE
# Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
# imprima la suma de ambos.
# ---------------------------------------------------------
print("\n--- EJERCICIO 2 ---")


# Tu código aquí:
def suma(a, b):
    sumar = a + b
    print(f"La suma de {a} y {b} es de {sumar}")


suma(45, 5)
# ---------------------------------------------------------
# EJERCICIO 3: ÁREA DEL RECTÁNGULO
# Escribe una función llamada "calcular_area_rectangulo" que tome dos
# parámetros "base" y "altura" y calcule el área.
# ---------------------------------------------------------
print("\n--- EJERCICIO 3 ---")


# Tu código aquí:
def calcular_area_rectangulo(base, altura):
    return base * altura


area = calcular_area_rectangulo(5, 5)
print(f"El área es de: {area}")

# ---------------------------------------------------------
# EJERCICIO 4: IMPRIMIR LISTA
# Define una función llamada "imprimir_lista" que tome una lista como
# parámetro y la imprima en la consola.
# ---------------------------------------------------------
print("\n--- EJERCICIO 4 ---")


# Tu código aquí:
def imprimir_lista(list=None):
    return list


print(imprimir_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ---------------------------------------------------------
# EJERCICIO 5: PAR O IMPAR
# Crea una función llamada "es_par" que tome un número como parámetro
# e imprima True si es par, o False si es impar.
# ---------------------------------------------------------
print("\n--- EJERCICIO 5 ---")


# Tu código aquí:
def es_par(num):
    return num % 2 == 0


print(es_par(9))

# ---------------------------------------------------------
# EJERCICIO 6: CONCATENACIÓN
# Escribe una función llamada "concatenar_strings" que tome dos
# parámetros "cadena1" y "cadena2" e imprima la concatenación de ambas.
# ---------------------------------------------------------
print("\n--- EJERCICIO 6 ---")


# Tu código aquí:
def concatenar_strings(cadena1, cadena2):
    print(cadena1 + " " + cadena2)


concatenar_strings("Hola", "Sergi")


# ---------------------------------------------------------
# EJERCICIO 7: EL MÁXIMO (OJO: Aquí pide DEVOLVER/RETURN)
# Define una función llamada "obtener_maximo" que tome una lista de
# números como parámetro y devuelva el número máximo de la lista.
# ---------------------------------------------------------
print("\n--- EJERCICIO 7 ---")


# Tu código aquí:
def obtener_maximo(list_numeros=None):
    if list_numeros is None:
        list_numeros = []
    return max(list_numeros)


print(obtener_maximo([1, 2, 3, 7, 8, 4, 234]))
# ---------------------------------------------------------
# EJERCICIO 8: FAHRENHEIT A CELSIUS (OJO: Pide DEVOLVER/RETURN)
# Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
# parámetro "fahrenheit" y devuelva su equivalente en Celsius.
# Fórmula: (F - 32) * 5/9
# ---------------------------------------------------------
print("\n--- EJERCICIO 8 ---")


# Tu código aquí:
def convertir_fahrenheit_a_celsius(f):
    c = (f - 32) * 5 / 9
    return c


print(convertir_fahrenheit_a_celsius(78))


# ---------------------------------------------------------
# EJERCICIO 9: CALCULADORA DE EDAD
# Escribe una función llamada "calcular_edad" que tome dos parámetros:
# "año_actual" y "año_nacimiento" y calcule la edad.
# ---------------------------------------------------------
print("\n--- EJERCICIO 9 ---")


# Tu código aquí:
def calcular_edad(año_actual, año_nacimiento):
    return año_actual - año_nacimiento


print(calcular_edad(2026, 1995))


# ---------------------------------------------------------
# EJERCICIO 10: DIVISIBILIDAD
# Define una función llamada "es_divisible" que tome dos parámetros
# "num" y "divisor" e imprima True si "num" es divisible por "divisor",
# o False si no lo es.
# ---------------------------------------------------------
print("\n--- EJERCICIO 10 ---")


# Tu código aquí:
def es_divisible(num, divisor):
    if num % divisor == 0:
        print(True)
    else:
        print(False)


es_divisible(5, 2)
# ---------------------------------------------------------
# EJERCICIO 11: INFO CON KEYWORDS
# Crea una función llamada "mostrar_info_persona" que tome tres
# argumentos de palabra clave: "nombre", "edad" y "ciudad".
# Imprime la información en un formato legible.
# ---------------------------------------------------------
print("\n--- EJERCICIO 11 ---")


# Tu código aquí:
def mostrar_info_person(nombre, edad, ciudad):
    print(f"Mi nombre es {nombre}, tengo {edad} años y soy de {ciudad}")


mostrar_info_person("Sergi", 31, "Barcelona")

# ---------------------------------------------------------
# EJERCICIO 12: PROMEDIO (Con valor por defecto)
# Escribe una función "calcular_promedio" que tome una lista de números.
# Si no se proporciona lista, debe usar una lista vacía por defecto.
# ---------------------------------------------------------
print("\n--- EJERCICIO 12 ---")


# Tu código aquí:
def calcular_promedio(numeros=None):
    # 1. PROTECCIÓN DE CREACIÓN (Patrón None)
    if numeros is None:
        numeros = []

    # 2. PROTECCIÓN LÓGICA (Evitar crash matemático)
    if not numeros:  # Si la lista está vacía (len == 0)
        return 0

    # 3. CÁLCULO SEGURO
    return sum(numeros) / len(numeros)


print(calcular_promedio([1, 3, 4, 5, 6, 7, 8, 9]))

# ---------------------------------------------------------
# EJERCICIO 13: POTENCIA (Con valor por defecto)
# Crea una función "calcular_potencia" que tome "base" y "exponente".
# Utiliza 2 como valor por defecto para el exponente.
# ---------------------------------------------------------
print("\n--- EJERCICIO 13 ---")
# Tu código aquí:


def calcular_potencia(base, exponente=2):
    p = base**exponente
    return p


print(calcular_potencia(4, 4))
# ---------------------------------------------------------
# EJERCICIO 14: FICHA DE ALUMNO (Mixto)
# Define "imprimir_info_alumno" que tome:
# - 1 argumento posicional: "nombre" (sin defecto)
# - 3 argumentos clave: "edad", "curso", "promedio" (con defecto None)
# Imprime la información legible.
# ---------------------------------------------------------
print("\n--- EJERCICIO 14 ---")


# Tu código aquí:
def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print(
        f"Mi nombre es {nombre} tengo {edad}, voy a clases de {curso} y mi promedio es de {promedio}"
    )


imprimir_info_alumno("Sergi")
