'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números impares.
'''

# Solicita números do intervalo
n1 = int(input('Digite o primeiro número do intervalo: '))
n2 = int(input('Digite o segundo número do intervalo: '))

# Estabelece as variáveis para contar os números e as listas para guardar os números
impares = 0
pares = 0
lista_impares = []
lista_pares = []

# Cria um loop para verificar se os números são ímpares ou pares, incrementa os contadores e adiciona na respectiva lista
for n in range(n1, n2 + 1):
    if (n % 2) != 0:
        impares += 1
        lista_impares.append(n)
    else:
        pares += 1
        lista_pares.append(n)

# Imprime o resultado
print(f'Nesse intevalo existem {impares} números ímpares.\nSão eles: {lista_impares}')
print(f'Nesse intevalo existem {pares} números pares.\nSão eles: {lista_pares}')
