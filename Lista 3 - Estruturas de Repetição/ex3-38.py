'''
Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''
# Importando a biblioteca para trabalhar com datas
from datetime import datetime

# Pede salário inicial e estabelece aumento
salario = float(input('Digite o salário inicial: R$'))
aumento = 0.015

# Loop para iterar de 1995 até a data atual. Note que no ano atual ele ainda não teve aumento
for i in range(1995, datetime.now().year):
    salario *= (1 + aumento)
    aumento *= 2

# Imprime salário atual
print(f'Salário atual: R${round(salario, 2)}')
