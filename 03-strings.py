nombre = 'martin leon'
edad = 25
correo = 'marodriguezl@hotmail.com'
texto = '      Este es un texto con muchos espacios a los lados         '

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
espacios = texto.strip()
empiezaPor = nombre.startswith('mar')
terminaPor = nombre.endswith('mar')
encontrar = nombre.find('i')
largo = len(nombre) #Cuenta desde 0 como un arreglo
indice = nombre.index('t')
tipo1 = nombre.isnumeric()
arreglo = nombre[3]
arregloCompuesto1 = nombre[4:9] #Trae del arreglo string los campos excluyendo la última posición
arregloCompuesto2 = nombre[:6] #Trae del arreglo string los campos desde el inicio hasta la posición indicada
arregloCompuesto3 = nombre[7:] #Trae del arreglo string los campos desde la posición indicada hasta el final del string

arregloInverso = nombre[-3]

print('Propiedades y Métodos de un String: \n',propiedadesMetodos)
print("-----------------------------------------" )
print("1. Tu nombre es " + nombre)
print(f"2. Tu nombre es {nombre}") #Agregar f al principio para que lo concatene en llaves. Desde la versión 3.6 de Python
print("3. Tu nombre es {}, tienes {} años y tu correo es {}".format(nombre,edad,correo)) #Otra forma de hacerlo

print("-----------------------------------------" )
print('Upper: ', mayus)
print('Lower: ',minus)
print('Title: ',title)
print('Capitalize: ',capi)
print('Replace: ',nuevoNombre)
print('Count: ',contarA)
print('1. Split Separar: ',separar)
print('2. Split Separar: ',separar2)
print('Con Espacios: ' + '/' + texto + '/' )
print('Strip Sin Espacios: ' + '/' + espacios + '/' )
print('startswith: ',empiezaPor)
print('endswith: ',terminaPor)
print('len largo: ',largo)
print('find: ',encontrar)
print('index: ',indice)
print('isnumeric: ',tipo1)
print('String Arreglo: ', arreglo)
print('arregloCompuesto1: ',arregloCompuesto1 )
print('arregloCompuesto2: ',arregloCompuesto2 )
print('arregloCompuesto3: ',arregloCompuesto3 )
print('arregloInverso: ',arregloInverso )
