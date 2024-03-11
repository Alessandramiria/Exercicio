'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

a = float(input('Determine a: '))
b = float(input('Determine b: '))
c = float(input('Determine c: '))

if a == 0:
    print('Com "a" igual a 0, a equação não é do segundo grau.')
    exit()

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print('Delta é negativo e a equação não possui raízes reais.')
    exit()

if delta == 0:
    x = (-b)/(2 * a)
    print('Delta é igual a zero e a equação possui apenas uma raiz real.')
    print(f'A raiz da equação é {x}')
    exit()

if delta > 0:
    x1 = (-b + delta)/(2 * a)
    x2 = (-b - delta)/(2 * a)
    print('Delta é maior que zero e a equação possui apenas duas raízes reais.')
    print(f'As raízes da equação são {x1} e {x2}')
    exit()
