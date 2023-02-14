ni = int(input("Ingrese el número inicial: "))
nf = int(input("Ingrese el número final: "))

cp = 0  # contador de números positivos
cn = 0  # contador de números negativos

for i in range(ni, nf+1):
    if i > 0:
        cp += 1
    elif i < 0:
        cn += 1

print("La cantidad de números positivos es:", cp)
print("La cantidad de números negativos es:", cn)