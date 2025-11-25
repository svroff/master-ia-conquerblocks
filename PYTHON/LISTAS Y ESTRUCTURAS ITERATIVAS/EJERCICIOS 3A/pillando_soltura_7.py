# 7. Crea un script que extraiga los elementos comunes entre dos listas. 

lista_1 = [3, 7, 12, 18, 25, 30, 45]
lista_2 = [5, 7, 10, 18, 22, 30, 50]
lista_3 = []

for n in lista_1:
    for m in lista_2:
        if n == m:
            lista_3.append(n)

print(lista_3)