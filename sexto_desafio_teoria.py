#Sexto desafio

cadena = input('Ingrese una cadena de caracteres: ')
cantidad = 0

for caracter in cadena:
    if caracter == 'a':
        cantidad += 1
    
print('La cantidad de de veces que aparece la letra \"a\" en la cadena ingresa es: {}'.format(cantidad))

# Otra forma es untilizar el metodo count que me devuelve la cantidad de veces que aparece un substring
# en un string 

print('La cantidad de de veces que aparece la letra \"a\" en la cadena ingresa es: {}'.format(cadena.count('a')))