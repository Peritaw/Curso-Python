#Funcion secundaria
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    palabraInvertida = palabra[::-1]

    if palabra == palabraInvertida:
        return True
    else:
        return False

#Funcion principal
def main():
    palabra = input('Ingrese una palabra: ')
    esPalindromo = palindromo(palabra)
    if esPalindromo:
        print('Es Palindromo')
    else: 
        print('No es palindromo')

#Punto de entrada de la aplicacion
if __name__ == '__main__':
    main()