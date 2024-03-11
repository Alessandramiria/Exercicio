'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos
deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de
dados deverá terminar quando for lido um número negativo.
'''

# Estabelece contadores e inicializa n como positivo
n = 1
g_0_25 = 0
g_26_50 = 0
g_51_75 = 0
g_76_100 = 0

# Enquanto n for maior que zero, repete o processo e soma um.
while n >= 0:
    n = int(input('Digite um número positivo: '))

    if (0 <= n <= 25):
        g_0_25 += 1

    elif (26 <= n <= 50):
        g_26_50 +=1

    elif (51 <= n <= 75):
        g_51_75 += 1

    elif (76 <= n <= 100):
        g_76_100 += 1

    else:
        pass

# Quando encerra o loop, imprime o resultado.
print(f'Existem {g_0_25} números no intervalo [0-25]\n'
      f'Existem {g_26_50} números no intervalo [26-50]\n'
      f'Existem {g_51_75} números no intervalo [51-75]\n'
      f'Existem {g_76_100} números no intervalo [76-100]\n')