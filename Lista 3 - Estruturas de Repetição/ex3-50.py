'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.
'''

# Pede a quantidade de termos e define a variável incremental da soma
n = int(input('Quantos termos deseja: '))
soma = 0

# Loop para incrementar a soma
for i in range(1, n + 1):
    soma += 1/i

print(round(soma, 2))