##Sets
###Un set es una colección que no posee órden, tampoco tiene números de índex. 
### Aparecen de forma aleatoria cada vez que llama:

colores = {'Amarillo','Verde','Rojo', 'Azul'}
print( 'set1: ', colores, type(colores), len(colores) )

##Agregar elementos a un set: 
###Lo pone en una posición aleatoria cada vez que se llama:
colores.add('Morado')

print('--------------------------------------------')
print( 'Agregar: ', colores, type(colores), len(colores) )

##Eliminar un elemento
colores.remove('Amarillo')

print('--------------------------------------------')
print( 'Eliminar: ', colores, type(colores), len(colores) )

##Limpiar el set:
colores.clear()
print('--------------------------------------------')
print( 'Limpiar: ', colores, type(colores), len(colores) )

###Eliminar el set
del colores
print('--------------------------------------------')
print( 'Eliminar: ', colores )