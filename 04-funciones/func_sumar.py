def sumar(*args, **kwargs):
    suma = 0 
    for n in args:
        suma += n
    return suma, kwargs


sumaTotal, datos = sumar(1,2,3,4,5,6, nombre = 'Luis', edad = 21)

print('La suma total es: ', sumaTotal)
print(datos)

