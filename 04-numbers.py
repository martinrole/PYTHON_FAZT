entero = 9
flotante = 14.4
flotante2 = 13. 

print( 'entero: ', type(entero) )
print( 'flotante: ', type(flotante) )
print( 'flotante2: ', type(flotante2) )
print( 'int a float', type( int(entero) ), float(entero) )
print( 'float a int', type( int(flotante) ), int(flotante) )

#Sumar
print( '---------------------' )
sumar = 2.0 + 1
print('Sumar', type(sumar), sumar)

#Restar
print( '---------------------' )
restar = 1 - 2.
print('Restar', type(restar), restar)

##División
print( '---------------------' )
division = 11 / 2
print( 'división: ', division )

##Operador de modulo: Devuelve el residuo de una división
## División entera o Euclídea
print( '---------------------' )
operadorModulo1 = 11 // 2
operadorModulo2 = 11 % 2

print( 'operadorModulo1: ', operadorModulo1 )
print( 'operadorModulo2: ', operadorModulo2 )

##Potencias de números:
print( '---------------------' )
potencia1 = 5 ** 3.0
potencia2 = pow(5,3)
print( 'potencia1: ', potencia1 )
print( 'potencia2: ', potencia2 )

##Numeros complejos
### Debe ir con con letra j para representar el número imaginario. No la letra i - Tomado por los ingenieros
print( '---------------------' )

complejo1 = 2 + 5j
complejo2 = 5j + 2
complejo3 = complex(2,5)
complejo4 = 7 + 11j
sumaCompleja = complejo1 + complejo4
multiCompleja = complejo1 * complejo4
conjugarComplejo = complejo4.conjugate()

print('Complejo1: ', type(complejo1), complejo1)
print('Complejo2: ', type(complejo2), complejo2)
print('Complejo3: ', type(complejo3), complejo3)

print('Complejo1 Parte Real: ', complejo1.real)
print('Complejo1 Parte Imaginaria: ', complejo1.imag)

print( '---------------------' )
print('Suma Compleja: ', sumaCompleja)
print('Multiplicación Compleja: ', multiCompleja) ## Hay una formula para multiplicar número complejos, no es dírecto
print('Conjugar Complejo: ', conjugarComplejo) ## Su espejo en el plano cartesiano


