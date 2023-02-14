n = int(input('Ingrese un numero: '))

suma = 0 
menores_n = 0 

while menores_n < n:
    suma += menores_n
    menores_n += 1

print('La suma es: ', suma)