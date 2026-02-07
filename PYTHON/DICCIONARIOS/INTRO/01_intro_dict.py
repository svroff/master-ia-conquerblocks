yo_mismo = {
    "nombre": "Sergi",
    "apellido" : "Vicente",
    "edad" : 34,
    "ciudad" : "Barcelona",
    "hobbies" : ["LoL", "Música", "Pokémon"]
}

print(yo_mismo)

print("Vivo en: ", yo_mismo["ciudad"])

print("Tengo ", yo_mismo["edad"], " años")

yo_mismo["edad"] = 30

print("Tengo ", yo_mismo["edad"], " años")


yo_mismo["trabajo"] = "Administrador de PACS"
print("Mi trabajo es: ", yo_mismo["trabajo"], " en el Clínic de Barcelona")

print("Mi segundo hobby es: ", yo_mismo["hobbies"][1])