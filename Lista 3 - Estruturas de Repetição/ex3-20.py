'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

# Define a condição para o while rodar
cont = 's'

# Enquanto desejar continuar, o sistema roda o cálculo do fatorial.
while cont == 's':
    n = int(input('Deseja calcular o fatorial de qual número? '))
    # Se o número estiver dentro do intervalo, estabelece a variável resultado para acumular as iterações
    if (0 < n < 16):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        print(f'O fatorial de {n} é {resultado}.')
        cont = str(input('Deseja continuar (s/n)? ')).lower()
    # Se o número estiver fora do intervalo, informa o usuário e reinicia o loop
    else:
        print('O número precisar ser inteiro, positivo e menor do que 16.')