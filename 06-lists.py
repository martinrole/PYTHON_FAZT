## Las listas se crean con []
from turtle import color


lista1 = [ 1,'hola',1.25, True,[1,2,3,4,5] ]
print('lista1: ', lista1, type(lista1))

##Utilizando el constructor:
###Un constructor es una función que permite definir una lista
lista2 = list( 'amarillo' )
print('lista2: ', lista2, type(lista2))

##Utilizando con tuplas
###Las tuplas se crean con ()
lista3 = list( (1,'hola',1.25, True,[1,2,3,4,5]) )
print('lista3: ', lista3, type(lista3))

##Crear una lista basada en un rango:
lista4 = list( range(1,11) )
print('lista4: ', lista4, type(lista4))

##Lo que puedo hacer con una lista, Los métodos que puedo utilizar:
print( '----------------------------------')
print( 'Métodos; ', dir(lista3))
print( 'Largo lista: ', len(lista3) )
print( 'Posición: ', lista3[4] )
print( 'Posición Inv: ', lista3[-1] )
print( 'Buscar: ', 'hola' in lista3 )

##Cambiar o reemplazar un elemento de una lista
print('----------------------------')
print( 'Sin cambio: ', lista3 )
lista3[0] = 'pepelinas'
print( 'Con cambio: ', lista3 )

##Agregar un elemento a la lista:
colores = ['amarillo']

print('-----------------------------')
print( 'Sin agregar: ', colores, len(colores) )

###Agregar un solo elemento en lista
colores.append('blanco')
print( 'Se agregó 1: ', colores, len(colores) )

###Agregar varios elementos al final de la lista
addVarios = colores.extend(('morado','azul', 'rojo'))
print( 'Se agregó 3: ', colores, len(colores) )

###ingresar elemento en posición indicada en lista:
colores.insert(1, 'agregado')
print( 'Agregado: ', colores, len(colores) )

##Eliminar elementos:

### eliminar el último elemento de la lista:
print('---------------------------')
print( 'Lista Actual: ', colores, len(colores) )
colores.pop()
print( 'Lista Eliminado: ', colores, len(colores) )

###Buscar y borrar elemento encontrado:
print('----------------------------')
print( 'Lista Actual: ', colores, len(colores) )
colores.remove('agregado')
print( 'Lista Eliminado: ', colores, len(colores) )

###eliminar elemento en posición indicada:
print('----------------------------')
print( 'Lista Actual: ', colores, len(colores) )
colores.pop(0)
print( 'Después de eliminar: ', colores, len(colores) )

###eliminar o limpiar toda la lista:
print('----------------------------')
print( 'Lista Actual: ', colores, len(colores) )
colores.clear()
print( 'Lista Ahora: ', colores, len(colores) )

###Ordenar una lista:
abc = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b','o','i','h']
num = [1,8,6,5,20,4,7,3,11,6]

print('----------------------------')
abc.sort()
num.sort()
print( 'Ordenar: ', abc )
print( 'Ordenar: ', num )
abc.sort(reverse=True)
num.sort(reverse=True)
print( 'Ordenar Inv: ', abc )
print( 'Ordenar Inv: ', num )

###Muestra el índice del primer elemento que cumpla la búsqueda:
print('----------------------------')
indice = num.index(6)
print( 'Indice: ', indice )

##Contar cuantas veces está un elemento:
contarItem = num.count(6)
print( 'Indice: ', contarItem )