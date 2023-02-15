import random

def generarPassword():
    mayusculas = ['A', 'B', 'C', 'F', 'G']
    minisculas = ['a', 'b', 'c', 'f', 'g']
    simbolos = ['#', '$', '%', '&', '/', '!', '¡']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minisculas + simbolos + numeros
    password = []

    for i in range(15):
        caracterRandom = random.choice(caracteres)
        password.append(caracterRandom)

    password = "".join(password)
    return password

def main():
    password = generarPassword()
    print('Tu nueva contraceña es: ', password)

if __name__ == '__main__':
    main()
