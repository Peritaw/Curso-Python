# Crear un programa que permita convertir una cantidad de segundos en horas, minutos y segundos.

# Análisis: Para la solución de este problema, se requiere que el usuario ingrese un tiempo expresado en segundos y el sistema procesa y obtiene las horas, minutos y segundos restantes.

hora = 3600
minuto = 60
t = (int(input('Ingrese un tiempo expresado en segundos: ')))
h = t // hora
t = t % hora
m = t // minuto
s = t % minuto

print('El tiempo restante es: ', h, ' horas, ', m, ' minutos, ', s, ' segundos')

print("luis \nstoller")
print("hol\na")