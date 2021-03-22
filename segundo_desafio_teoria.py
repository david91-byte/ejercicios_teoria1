
#Segundo desafio

numero2 = int(input('Ingrese un numero entero: '))

if numero2 % 2 == 0 or numero2 % 3 == 0 or numero2 % 5 == 0:
    if numero2 % 2 == 0:
        print(f'El numero {numero2} es divisible por 2')
    if numero2 % 3 == 0:
        print('El numero {} es divisible por 3'.format(numero2))
    if numero2 % 5 == 0:
        print(f'El numero {numero2} es divisible por 5')
else:
    print('El numero {} no es divisible ni por 2, ni por 3, ni por 5'.format(numero2))