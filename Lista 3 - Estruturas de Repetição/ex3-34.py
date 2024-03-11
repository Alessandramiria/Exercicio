'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa
que peça um número inteiro e determine se ele é ou não um número primo.
'''

# Solicita o número e estabelece uma variável de controle como true
n = int(input('Digite o número desejado: '))
primo = True

# Verifica se o número informado possui alguma divisão com resto zero. Excetuando o número 1 e o próprio número.
for i in range(2, n):
    resto = n % i
    # Se possuir alguma divisão com resto zero, não é primo.
    if (resto == 0):
        primo = False

if (primo):
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
