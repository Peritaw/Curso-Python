numeroInicial = int(input('Ingrese el numero inicial: '))
numeroFinal = int(input('Ingrese el numero final: '))

i = 0
contador = 0

i = numeroInicial + 1
while i < numeroFinal:
    contador += 1
    i += 1

print('La cantidad es: ', contador)