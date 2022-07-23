numero = input('Ingrese un número: ')
##Todo valor ingresado entra como un string:
print(type(numero))

## El condicional debe tener un espacio o tab en la siguiente linea del if
if float(numero) < 0:
    print("El número es negativo")
elif float(numero) > 0 and float(numero) <= 5:
    print("El número esta entre 0 y 5")
elif float(numero) > 5 and float(numero) <= 10:
    print("El número está entre 6 y 10")
else:
    print("El número es mayor a 10")