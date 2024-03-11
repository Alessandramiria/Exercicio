'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''


# Solicita quantos números serão adicionados ao conjunto
qntd = int(input('Quantos números deseja adicionar? '))
# Define o conjunto, incialmente vazio
lista = []

# Adiona os números inteiros ao conjunto um a um.
for i in range(0, qntd):
    n = int(input(f'Digite o {i + 1}° número: '))
    # Enquanto o número adicionado estiver fora do intervalo, solicita um novo valor
    while n < 0 or n > 1000:
        print('O valores devem pertencer ao intervalo de 0 a 1000')
        n = int(input(f'Digite o {i + 1}° número: '))
    # O 'append' está fora do while e só adiciona o número a lista apenas quando estiver dentro do intervalo
    lista.append(n)

# Imprime a soma, o maior e o menor valor do conjunto
print(f'A soma dos números do conjunto é {sum(lista)}')
print(f'O maior valor do conjuto é: {max(lista)}')
print(f'O menor número do conjunto é: {min(lista)}')