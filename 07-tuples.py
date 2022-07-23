##Las tuplas o Tuples 
### Permiten definir un conjunto de datos que no se puede cambiar como las listas
### Son más rápidas que las listas para el PC

tupla = (1,'hola', True, [1,2,3] )
print('Tupla1: ', tupla, type(tupla), len(tupla) )

##Crear tupla con función:
tupla2 = tuple('amarillo')
tupla3 = tuple( ('amarillo') )
tupla4 = tuple( ('amarillo','rojo','azul') )

print('----------------------------------' )
print('Tupla2: ', tupla2, type(tupla2), len(tupla2) )
print('Tupla3: ', tupla3, type(tupla3), len(tupla3) )
print('Tupla4: ', tupla4, type(tupla4), len(tupla4) )

##Una tupla siempre debe tener 2 0 más elementos:
###Si coloco un elemento no crea la tupla sino lo toma como un datatype
print('----------------------------------' )
tuplita = ('Un Elemento')
print('Tuplita: ', tuplita, type(tuplita) )

###Para crear una tupla de un solo elemento se usa una coma:
tuplita2 = ('Un Elemento',)
print('Tuplita2: ', tuplita2, type(tuplita), len(tuplita2) )

##Se puede acceder a un elemento igual que las listas:
nuevaTupla = ('amarillo','verde','azul','rojo')
posicion = nuevaTupla[2]
print('Elemento Tupla: ', posicion )

##Las funciones y métodos que se pueden aplicar a la tuplas
###Salen menos métodos en comparación a una lista
print('----------------------------------' )
print('Métodos: ', dir(tupla2) )


##Eliminar una tupla completamente, 
###No se puede limpiar como las listas:
del nuevaTupla
print('----------------------------------' )
print('No existe tupla: ', nuevaTupla )

