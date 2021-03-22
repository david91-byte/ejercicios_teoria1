# Quinto desafio

cadena1 = input('Ingrese una primer cadena de caracteres; ')
cadena2 = input('Ingrese una segunda cadena de caracteres: ')

#Se utiliza la funcion len para saber el tamanio de la cadena ingresada

if len(cadena1) > len(cadena2):
    print('La cadena {0} es mas larga que la cadena {1}'.format(
        cadena1, cadena2))
elif len(cadena2) > len(cadena1):
    print('La cadena {0} es mas larga que la cadena {1}'.format(
        cadena2, cadena1))
else:
    print('La cadena {0} y la cadena {1} son igual de largas'.format(
        cadena1, cadena2))
