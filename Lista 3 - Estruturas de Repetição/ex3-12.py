'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''
# Solicitando número que o usuário deseja ver a tabuada
n_tabuada = int(input('Deseja ver a tabuada de qual número? '))

# Imprimindo uma vez o cabeçalho da tabuada
print(f'Tabuada de {n_tabuada}:')

# Imprimindo a tabuada do número desejado
for n in range(1, 11):
    print(f'{n_tabuada} X {n} = {n_tabuada * n}')