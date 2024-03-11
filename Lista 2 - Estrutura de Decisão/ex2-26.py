"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro e acima de 20 litros, desconto de 5% por litro
Gasolina: até 20 litros, desconto de 4% por litro e acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

print('Que combustível deseja?')
tipo = str(input('[A] Álcool\n[G] Gasolina\n')).upper()
litros = float(input('Quantos litros deseja abastecer? '))

p_alcool = 1.90
p_gasolina = 2.50
custo = 0

if tipo == 'A':
    if litros <=  20:
        custo = (p_alcool * litros) * 0.97
    else:
        custo = (p_alcool * litros) * 0.95
if tipo == 'G':
    if litros <=  30:
        custo = (p_gasolina * litros) * 0.96
    else:
        custo = (p_gasolina * litros) * 0.94

print('R${:.2f}'.format(custo))
