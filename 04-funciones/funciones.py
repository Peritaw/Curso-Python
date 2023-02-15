def saludar():
    global nombre
    nombre = 'Luis Stoller'
    print('Hola desde la funcion saludar')
    print('Hola ', nombre)

saludar()
print('Hola desde afuera de la funcion', nombre)