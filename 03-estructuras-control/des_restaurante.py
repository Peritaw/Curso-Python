#Entrada
consumo = float(input('Ingrese el consumo del cliente: '))


#Proceso
if consumo >=0:
    if consumo <= 100:
        #Descuento 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        #Descuento 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200:
        #Descuento 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30

    monto_descuento = consumo - descuento

    igv = monto_descuento * 0.19
    total_pagar = monto_descuento + igv

    #Salida de datos 
    print('='*30)
    print('----- FACTURA DE CONSUMO -----')
    print('Descuento que se aplica: ', dato_descuento)
    print('='*30)
    print('Consumo: ', consumo)
    print('Descuento: ', descuento)
    print('Monto con descuento: ', monto_descuento)
    print('IGV: ', igv)
    print('Total a pagar: ', total_pagar)
    print('='*30)

else:
    print('Error al ingresar el consumo')



