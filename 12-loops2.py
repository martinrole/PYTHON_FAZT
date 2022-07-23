numero = input("Ingresa un número: ")

print('---------------------------')
for i in range(1,int(numero)):
    print(i)

print('---------------------------')
contador = 1

while contador < int(numero):
    print(contador)
    contador = contador + 1

print('---------------------------')
contador = 1

while contador < int(numero):
    print(contador)
    contador += 1
    
print('---------------------------')
numero2 = input("Ingresa número. Si pones 1 ingresa al ciclo")

while numero2 == '1':
    print("Entra en ciclo")
    numero2 = input("Ingresa un número otra vez: ")