"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

kg_morango = float(input('Quantos kilos de morango? '))
kg_maca = float(input('Quantos kilos de maça? '))

if kg_morango <= 5:
    custo_morango = kg_morango * 2.50
else:
    custo_morango = kg_morango * 2.20

if kg_maca <= 5:
    custo_maca = kg_maca * 1.80
else:
    custo_maca = kg_maca * 1.50

custo_total = custo_maca + custo_morango
kg_total = kg_maca + kg_morango

if custo_total > 25 or kg_total > 8:
    custo_total = custo_total * 0.9

print('Valor das compras: R${:.2f}'.format(custo_total))