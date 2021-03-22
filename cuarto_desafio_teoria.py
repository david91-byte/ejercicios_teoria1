#Cuarto desafio

caracter = input('Ingrese un caracter: ')

if caracter == '\"' or caracter == '\'':
    print ('El caracter \"{}\" ingresado , es una comilla '.format(caracter))
else:
    print(f'El caracter \"{caracter}\" no son comillas')