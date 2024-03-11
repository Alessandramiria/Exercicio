'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''

# Define as listas para armazenar os números
numeros = []
par = []
impar = []

# Loop para solicitar os números
for i in range(0, 20):
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)

    # Se o resto da divisão por 2 por diferente de 0 o número é ímpar, caso contráiro é par
    if numeros[i]%2 != 0:
        impar.append(n)
    else:
        par.append(n)

# Imprime resultados
print(f'Vetor completo: {numeros}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
