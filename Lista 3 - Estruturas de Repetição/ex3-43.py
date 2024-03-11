'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

# Dicionário com cardápio
cardapio = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.30, 105: 1.00}

# Incializa o pedido, o total e a continuação do while
pedido = {}
total = 0
cont = 1

while cont == 1:

    # Pede o item e a quantidade
    item = int(input('Digite o código do pedido: '))
    qntd = int(input('Digite a quantidade: '))

    # Adiciona o item e seu o total (quantidade * preço)
    pedido[item] = round(cardapio.get(item) * qntd, 2)

    # Incrementa o total geral
    total += round(cardapio.get(item) * qntd, 2)

    cont = int(input('Deseje pedir mais alguma coisa:\n[1] - Sim\n[2] - Não\n'))

# Imprime pedido quando sair do loop
print('-=' * 11)
print(' Resumo pedido')
print('-=' * 11)
print('Item     Total Item(R$)')
for item in pedido:
    print(f'{item}          {pedido[item]:.2f}')

print('-' * 25)
print(f'Total do pedido: R$ {total:.2f}')
