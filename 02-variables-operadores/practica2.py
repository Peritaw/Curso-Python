# Practica 02: Calcular el Precio de Venta
# Enunciado: dado el valor de venta de productos, hallar el IGV (18%) y el precio de venta.

# Análisis: para la solución de este problema, se requiere que el usuario ingrese el valor de venta del producto y el sistema realice el cálculo respectivo para hallar el IGV y el precio de venta, para esto use la siguiente expresión.

print('=====REALIZAR UNA VENTA=====')
producto = int(input('Ingrese el valor de venta del producto: '))
igv = 0.18

valor_igv = producto * igv 
precio_venta = valor_igv + producto

print('El valor del IGV para este producto es de: ', valor_igv, ' El precio de venta final para este producto es: ', precio_venta)
