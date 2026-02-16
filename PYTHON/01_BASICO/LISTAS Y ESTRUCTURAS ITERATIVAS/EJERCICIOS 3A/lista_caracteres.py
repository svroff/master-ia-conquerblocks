frutas = ['manzana', 'platano', 'cereza', 'pera', 'higo', 'frambuesa', 'fresa']
print('-------------------------------------------------------')
print(len(frutas))
print('-------------------------------------------------------')
print(frutas[2])
frutas[1] = 'mora'
print('-------------------------------------------------------')
print(frutas[2])
frutas.append('mango')
frutas.insert(0, 'uva')
 
ultima_fruta = frutas.pop()
print('-------------------------------------------------------')
print(ultima_fruta)
print('-------------------------------------------------------')
for f in frutas:
    print(f, len(f))
print('-------------------------------------------------------')
for f in frutas:
    if len(f) > 5:
        print(f, len(f))
frutas.remove('cereza')
frutas.clear()
