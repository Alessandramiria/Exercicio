'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o numero
seja inválido e continue pedindo até que o usuário informe um numero válido.
'''

# Pede número ao usuário
numero = float(input('Digite um número entre 0 e 10: '))

# Enquanto número informado for menor que 0 ou maior que 10, informa o usuário e solicita o número novamente
while (numero > 10 or numero < 0):
    print(f'O número {numero} é inválido')
    numero = float(input('Digite um novo número: '))

print('O número digitado é válido.')