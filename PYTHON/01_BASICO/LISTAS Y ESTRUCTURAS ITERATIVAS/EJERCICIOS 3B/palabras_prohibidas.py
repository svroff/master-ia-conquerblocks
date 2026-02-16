'''
PALABRAS PROHIBIDAS: 

Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. 
Filtra las palabras en tu lista original y crea una nueva lista de palabras filtradas que solo contenga 
aquellas palabras que no tienen ninguna letra prohibida.

'''
# creamos las listas que nos pide el enunciado.
lista_palabras = ['Python', 'Cloud', 'Syngovia', 'Guantes', 'Mandarinas', 'Barceloty']
lista_letras = ['y', 'o', 'b', "hola"]
lista_palabras_filtradas = []


# creamos los bucles para iterar en ambas listas.
for p in lista_palabras:
    tiene_letra_prohibida = False
    for l in lista_letras:
        if l in p.lower():
            tiene_letra_prohibida = True
            break
        if not tiene_letra_prohibida and p not in lista_palabras_filtradas:
            lista_palabras_filtradas.append(p)
            

print(lista_palabras_filtradas)