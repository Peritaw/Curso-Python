import random

def jugar(vidas):
    numeroRandom = random.randint(1, 100)
    numeroElegido = None

    while numeroRandom != numeroElegido:
        numeroElegido = int(input('Ingrese un numero entre 1 y 100: '))

        if numeroRandom < numeroElegido:
            print('Elige un numero mas pequeño')
            vidas -= 1
        elif numeroRandom > numeroElegido:
            print('Elige un numero mas grande')
            vidas -= 1

        if vidas == 0:
            print('GAME OVER')
            break

        print(f'Te quedan {vidas} vidas')

    if numeroElegido == numeroRandom: 
        print('FELICIDADES GANASTE')

def main():
    while True:
        menu = """
        ADIVINA EL NÚMERO ALEATORIO
        1 - Nivel facil
        2 - Nivel Intermedio 
        3 - Nivel Dificil
        4 - Salir
        INGRESA UNA OPCIÓN: """

        opcion = input(menu)

        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print('CERRANDO JUEGO')
            break
        else:
            print('OPCION INCORRECTA VUELVA A INGRESAR UN NUMERO VALIDO')


if __name__ == '__main__':
    main()
