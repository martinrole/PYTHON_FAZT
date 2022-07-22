#String
print (type("Hello World"))

#integer
print(type(10))

#float
print(type(30.5))

#boolean
print(type(True))

#list: Si se puede cambiar
print(type([10,"hola",30,"mundo"]))

#Tuples (Tuplas): Es una lista que no puede cambiar
print(type((10,20,30,55)))

# Dictorionies: (Diccionarios) Permite agrupar datos que pertenecen a una misma entidad: Key: Value
persona = {
    "nombre": "Ramón",
    "apellido": "Valdez",
    "apodo": "Ron Damón",
    "edad": 45
}

print(type(persona))

# None
print( type(None) )
