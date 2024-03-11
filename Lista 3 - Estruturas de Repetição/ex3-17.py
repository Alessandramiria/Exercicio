'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

# Solicita número para iterar
n = int(input('Digite o número que deseja calcular o fatorial: '))

# Estabelece a variável que que vai guardar o valor para cada iteração
resultado = 1

# Loop para multiplicar por todos os números até o valor desejado
for i in range(1, n +1):
    resultado *= i

print(f'O fatorial de {n} é {resultado}.')