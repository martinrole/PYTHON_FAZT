 # Def es def de funcion

def saludo(nombre="Sin nombre"):
    print("Hola " + nombre )

saludo('Martin')

def agregar(num1, num2):
    return num1 + num2

print( agregar(10,30) )

##Funciones Lambda: 
### Son una forma corta de declarar funciones pequeñas y anónimas

adicionar = lambda num1, num2: num1 + num2

print( adicionar(34,22) )