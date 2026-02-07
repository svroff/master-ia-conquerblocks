# Tienes una lista de palabras
palabras = ["mesa", "mapa", "silla", "sopa", "miel"]

# Quieres agruparlas por su LETRA INICIAL
# Resultado esperado: { "m": ["mesa", "mapa", "miel"], "s": ["silla", "sopa"] }

agrupador = {}

for p in palabras:
    letra = p[0]  # Sacamos la primera letra (ej: "m")

    # --- AQUÍ FALTA TU LÓGICA NUEVA ---
    # 1. Pregunta: ¿Esta letra NO está en las claves de 'agrupador'?
    if letra not in agrupador:
        # 2. Si es cierto (no está): Crea una lista vacía en esa clave.
        agrupador[letra] = []
    # --- FIN DE TU LÓGICA ---

    # 3. Ahora que seguro que existe, añade la palabra
    agrupador[letra].append(p)

print(agrupador)
