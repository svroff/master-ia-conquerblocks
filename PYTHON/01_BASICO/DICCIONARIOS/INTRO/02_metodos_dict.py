mi_inventario = {
    "pociones" : 3,
    "espada" : "excalibur",
    "monedas" : 150
}

print(f'Sergi quiere equiparse con un escudo llamado {mi_inventario.get("escudo", "No tiene escudo")}')

print(f'Mi inventario tiene {list(mi_inventario.keys())}')

item_vendido = mi_inventario.pop("espada")

print(f'Has vendido tu {item_vendido}')

print("\n--- REVISANDO LA MOCHILA ---")

for item, quantity in mi_inventario.items():
    print(f'{item} : {quantity}')