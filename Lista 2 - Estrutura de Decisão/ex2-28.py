"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara
o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o
tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações
da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

print('Que tipo de carne você deseja? ')
carnes = {0:'File Duplo', 1:'Alcantra', 2:'Picanha'}
codigo_carne = int(input('[0] File Duplo\n[1] Alcatra\n[2] Picanha\n'))
kg_carne = float(input('Quantos kilos deseja? '))
valor_compra = 0.0

if (kg_carne <= 5):
    if (codigo_carne == 0):
        valor_compra = kg_carne * 4.9
    elif (codigo_carne == 1):
        valor_compra = kg_carne * 5.9
    elif (codigo_carne == 2):
        valor_compra = kg_carne * 6.9

if (kg_carne > 5):
    if (codigo_carne == 0):
        valor_compra = kg_carne * 5.8
    elif (codigo_carne == 1):
        valor_compra = kg_carne * 6.8
    elif (codigo_carne == 2):
        valor_compra = kg_carne * 7.8

valor_compra = round(valor_compra, 2)
print('Deseja pagar com o Cartão Tabajara?')
cartao_tabajara = int(input('[0] Sim\n[1] Não\n'))

desconto = round(valor_compra * 0.05 if cartao_tabajara == 0 else 0, 2)

valor_final = round(valor_compra - desconto, 2)

print('-' * 25)
print('CUPOM FISCAL')
print('-' * 25)
print(f'Item: {carnes.get(codigo_carne)}\nQuantidade: {kg_carne}kgs\n'
      f'Forma de pgto: {"Cartão Tabajara" if cartao_tabajara == 0 else "Outro"}\n'
      f'Valor total: R${valor_compra}\nDesconto: R${desconto}\nValor final: R${valor_final}' )
print('-' * 25)
