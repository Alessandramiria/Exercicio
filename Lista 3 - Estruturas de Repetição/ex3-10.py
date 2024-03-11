'''
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
'''

# Solicitando os números do intervalo
n1 = int(input('Digite o menor número do intervalo: '))
n2 = int(input('Digite o maior número do intervalo: '))

# Definindo a função range com os números do invervalo
for n in range(n1, n2 +1):
    print(n)
