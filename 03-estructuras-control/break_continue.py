c = 0

while c < 10:
    c += 1 
    print(c)

    if c == 5:
        # print("Termina el bucle")
        print("Salta a siguiente iteracion")
        # break
        continue
    print('Despues de continue')
else:
    print('Fin del bucle')