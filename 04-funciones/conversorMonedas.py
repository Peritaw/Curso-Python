def convertir(valor_dolar, pais):
    cantidadMoneda = float(input(f'Ingrese cantidad de {pais}: '))

    dolares = cantidadMoneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'Tienes ${dolares} Dolares')


def main():
    while True:
        menu = """
        1-Pesos Argentinos a Dolares
        2-Pesos Mexicanos a Dolares
        3-Pesos Colombianos a Dolares
        4-Salir
        Ingrese una Opcion"""
        
        opcion = input(menu)

        if opcion == '1':
            convertir(372, 'persos argentinos')
        elif opcion == '2':
            convertir(20, 'persos mexicanos')
        elif opcion == '3':
            convertir(3471.27, 'persos colombianos')
        elif opcion == '4':
            print('Cerrando conversor de monedas')
            break
        else: 
            print('Opcion incorrecta !!!')
            print('Vuelve a ingresar la opcion correcta')

if __name__ == '__main__':
    main()
            

    