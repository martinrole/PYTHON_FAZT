edad = input('Igresa edad: ')
altura = float( input('Igresa edad: ') )

##Todo ingresa como si fuera un string:
print( type(edad) )
print( type(altura) )

##Tengo que convertir en un número para hacer operaciones matemáticas:
print('---------------------------------------')
nuevaEdad = int(edad) + 5
print( nuevaEdad )