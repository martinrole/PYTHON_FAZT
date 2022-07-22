nombre = 'martin leon'

#dir() retorna todas las propiedades y metodos de un objeto
propiedadesMetodos = dir(nombre)

#
mayus = nombre.upper()
minus = nombre.lower()
title = nombre.title()
capi = nombre.capitalize()
nuevoNombre = nombre.replace('leon','rodriguez').upper()
contarA = nombre.count('a')
separar = nombre.split() #Separa por caracter en blanco y crea una lista
separar2 = nombre.split('l') #Separa por caracter y crea una lista
empiezaPor = nombre.startswith('mar')
terminaPor = nombre.endswith('mar')
encontrar = nombre.find('i')
largo = len(nombre) #Cuenta desde 0 como un arreglo
indice = nombre.index('t')
tipo1 = nombre.isnumeric()
arreglo = nombre[3]
arregloInverso = nombre[-3]

#print(propiedadesMetodos)
print("Tu nombre es " + nombre)
print(f"Tu nombre es {nombre}") #Agregar f al principio para que lo concatene en llaves. Desde la versión 3.6 de Python
print("Tu nombre es {0}".format(nombre)) #Otra forma de hacerlo


print(mayus)
print(minus)
print(capi)
print(nuevoNombre)
print(contarA)
print(separar)
print(separar2)
print(empiezaPor)
print(terminaPor)
print(largo)
print(encontrar)
print(indice)
print(tipo1)
print(arreglo)
print(arregloInverso)
