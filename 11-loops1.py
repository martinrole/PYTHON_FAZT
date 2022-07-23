##Bucles o Loops
colores = ['Amarillo','Rojo','Verde','Azul','Amarillo','Morado','Blanco']

print('-------------------')
for item in colores:
    print(item)

print('-------------------')
for color in colores:
    if (color == 'Morado'):
        print('Color')
    print(color)

print('-------------------')
for color in colores:
    if (color == 'Morado'):
        break ##para el Proceso
    print(color)

print('-------------------')
for color in colores:
    if ( color == 'Amarillo'):
        continue ##Es como si se lo saltara
    print(color)