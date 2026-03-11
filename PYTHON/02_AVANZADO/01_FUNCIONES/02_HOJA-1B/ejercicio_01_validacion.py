# ==========================================
# EJERCICIO 1: VALIDACIÓN DE FORMULARIO
# ==========================================
# Crea una función llamada "validar_formulario" que reciba:
# - nombre, correo electrónico y número de teléfono.
#
# Debe verificar las siguientes reglas:
# 1. El nombre debe tener una longitud mínima de 3 caracteres[cite: 845].
# 2. El teléfono debe estar conformado por dígitos y tener una longitud de 9 caracteres[cite: 846].
# 3. El email debe contener un "@" y un "."[cite: 847].
#
# La función debe devolver True si todo es correcto, o False (o imprimir el error) si falla.


print("\n--- EJERCICIO 1: FORMULARIO ---")

# Tu código aquí:


# creamos la función
def validar_formulario(nombre, email, telefono):
    if (
        len(nombre) >= 3
        and telefono.isdigit()
        and len(telefono) == 9
        and "@" in email
        and "." in email
    ):
        return True
    else:
        return False


primera_prueba = validar_formulario("Sergi", "correo@correo.es", "535353535")
print(primera_prueba)
