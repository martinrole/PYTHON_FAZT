##Dictionarios sirve para defirni objetos:
carrito = {
    {
        'producto': 'nombreLibro 1',
        'cant': 3,
        'precio': 20000
    },
    {
        'producto': 'nombreLibro 2',
        'cant': 1,
        'precio': 17500
    }
}

usuario = {
    'nombre': 'nombreUsuario',
    'correo': 'correo@hotmail.com',
    'fechaNacimiento': '1992-03-28' ,
    'perfil': 'administrador'
}

print('Dictionary: ', usuario, type(usuario), len(usuario) )

##Ver todas las keys de un objeto:
print('--------------------------------')
llaves = usuario.keys()
print('Llaves: ', llaves, type(llaves), len(llaves) )

##Conseguir valor de una clave del objeto:
print('--------------------------------')
valor = usuario.get('fechaNacimiento')
print('Valor: ', valor, type(valor), len(valor) )

##Ver todos los valores de las keys del objeto:
###Los muestra dentro de una tupla
print('--------------------------------')
valores = usuario.items()
print('Valores: ', valores, type(valores), len(valores) )

###Agregar un valor al objeto:
print('--------------------------------')
print('Antes Add: ', usuario, type(usuario), len(usuario) )
usuario["estatura"] = 1.85
print('Después Add: ', usuario, type(usuario), len(usuario) )

###Actualiar un valor del objeto:
print('--------------------------------')
print('Antes Actualizar: ', usuario, type(usuario), len(usuario) )
usuario["nombre"] = 'Tobias León'
print('Después Actualizar: ', usuario, type(usuario), len(usuario) )

##Ver todas las funciones y métodos que se pueden aplicar:
print('--------------------------------')
print('Métodos: ', dir(carrito) )