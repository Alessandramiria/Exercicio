'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

# Solicitando os números do intervalo
n1 = int(input('Digite o menor número do intervalo: '))
n2 = int(input('Digite o maior número do intervalo: '))
intervalo = []

# Definindo a função range com os números do invervalo
for n in range(n1, n2 +1):
    print(n)
    intervalo.append(n)

print(f'A soma do intervalo é: {sum(intervalo)}')
