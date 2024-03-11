"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('Que operação deseja realizar:')
operacao = int(input('[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n'))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1 * n2
elif operacao == 4:
    resultado = n1 / n2
else:
    print('Operação inválida.')

p_i = 'par' if resultado % 2 == 0 else 'impar'
p_n = 'positivo' if resultado > 0 else 'negativo'
i_d = 'inteiro' if resultado.is_integer() else 'decimal'

print(f'O resultado da operação é {resultado}. O número é {p_i}, {p_n} e {i_d}.')



