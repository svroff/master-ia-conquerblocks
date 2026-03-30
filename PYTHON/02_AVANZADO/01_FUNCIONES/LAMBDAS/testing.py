nombres = ["Ana", "Pedro", "Al", "Sofía", "Jo"]
# Filtra los nombres que tengan más de 3 caracteres usando filter + lambda. Sin definir ninguna función con def.

filtro = list(filter(lambda x: len(x) > 3, nombres))
print(filtro)
