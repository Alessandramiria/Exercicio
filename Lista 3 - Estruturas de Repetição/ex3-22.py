'''
Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
'''

# Solicita o número e estabelece uma variável de controle como true
n = int(input('Digite o número desejado: '))
primo = True
lista_divisores = []

# Verifica se o número informado possui alguma divisão com resto zero. Excetuando o 1 e o próprio número.
for i in range(2, n):
    resto = n % i
    # Se possuir alguma divisão com resto zero, não é primo.
    if (resto == 0):
        # Adiciona todos os divisores com resto 0, a lista
        lista_divisores.append(i)
        primo = False

if (primo):
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo e seus divisores são:\n{lista_divisores}')
