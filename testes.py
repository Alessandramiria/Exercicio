
parcelas = {1: 0, 3: 0.1, 6: 15, 9: 20, 12: 25}
divida = float(input('Digite o valor da dívida: '))

print('Valor da Dívida / Valor dos Juros / Qtnd Parcelas / Valor Parcelas')

for i in parcelas.keys():
    print(parcelas.get(i))