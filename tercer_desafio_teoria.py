#Tercer desafio

letra = input('Ingrese una letras desde el teclado: ')

if letras >= 'a' and letra <= 'z':
    print(f'La letra \"{letra}\" esta en minuscula')
else letra >= 'A' and letra <= 'Z':
    print('La letra \"{}\" ingresada esta en mayuscula'.format(letra))
    
#Otra forma es utilizar la funcion upper(), que convierte un caracter o una cadena de caracteres a mayuscula
#La funcion opuesta en lower que convierte todo a minuscula
#De esta forma comparo si la letra ingresada es igual a esa letra en mayuscula

if letra == letra.upper():
    print('La letra \"{}\" ingresada esta en mayuscula'.format(letra))
else:
    print(f'La letra \"{letra}\" esta en minuscula')
    
#Otra forma es utilizando la funcion isupper o islower, que nos devuelve true si la 
#la letra esta en mayuscula o en minuscula respectivamente, o false si es el caso contrario

if letra.islower():
     print(f'La letra \"{letra}\" esta en minuscula')
else:
    print('La letra \"{}\" ingresada esta en mayuscula'.format(letra))