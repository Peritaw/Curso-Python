suma = lambda a,b:a+b
doblar = lambda n: n * 2
par = lambda n: n % 2 == 0
impar = lambda n: n % 2 != 0
revertir = lambda cadena: cadena[::-1]

print(suma(10, 20))
print(doblar(10))
print(par(4))
print(impar(7))
print(revertir('alfin te pusiste a laburar vago'))