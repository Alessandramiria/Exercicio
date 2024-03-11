'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
'''

# Pede a quantidade de termos e define a variável incremental da soma e do denominador
n = int(input('Quantos termos deseja: '))
soma = 0
denominador = 1

# Loop para incrementar a soma e o denominador e imprimir os termos
print('S = ', end='')
for i in range(1, n + 1):
    print(f'{i}/{denominador}', end='')
    soma += i/denominador
    denominador += 2
    if i < n:
        print(' + ', end='')
    else:
        print('')

print(f'S = {round(soma, 2)}')