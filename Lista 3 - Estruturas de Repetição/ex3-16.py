'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''

# Estabelece os dois primeiros elementos da sequencia de Fibonacci
lista = [0, 1]

# Estabele o contador que vai iterar com a posição da lista
n = 0

# Itera elementos da lista enquanto o seu último elemento for menor do que 500
while lista[-1] < 500:
    lista.append(lista[n] + lista[n + 1])
    n += 1
print(lista)