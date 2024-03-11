'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas / % de Juros sobre o valor inicial da dívida
1                           0
3                           10
6                           15
9                           20
12                          25

Exemplo de saída do programa:
Valor da Dívida / Valor dos Juros / Quantidade de Parcelas / Valor da Parcela
R$ 1.000,00         0               1                       R$  1.000,00
R$ 1.100,00         100             3                       R$    366,00
R$ 1.150,00         150             6                       R$    191,67
'''

# Cria dicionário com parcelas e respectivos juros e pede a divida
parcelas = {1: 0.0, 3: 0.1, 6: 0.15, 9: 0.20, 12: 0.25}
divida = float(input('Digite o valor da dívida: '))

# Imrpime cabeçalho
print('Valor da Dívida / Valor dos Juros / Qtnd Parcelas / Valor Parcelas')

# Para cada valor na chave dos dicionários imprime uma linha
for i in parcelas.keys():
    print(f'{divida * (1 + parcelas.get(i))}            '
          f'{parcelas.get(i) * 100}%                '
          f'{i}               '
          f'{divida if parcelas.get(i)== 0 else round(((divida * (1 + parcelas.get(i))) / i), 2)}')
