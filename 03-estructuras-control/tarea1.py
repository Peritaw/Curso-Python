n1 = float(input('Ingrese el primer numero: '))
n2 = float(input('Ingrese el segundo numero: '))
n3 = float(input('Ingrese el tercer numero: '))

if n1 > n2 and n1 > n3 :
    if n2 > n3:
        print('Numeros ordenados: ', n1, n2, n3)
    else:
        print('Numeros ordenados: ', n1, n3, n2)
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print('Numeros ordenados: ', n2, n1, n3)
    else:
        print('Numeros ordenados: ', n2, n3, n1)
if n3 > n1 and n3 > n2:
    if n1 > n2:
        print('Numeros ordenados: ', n3, n1, n2)
    else:
        print('Numeros ordenados: ', n3, n2, n1)
