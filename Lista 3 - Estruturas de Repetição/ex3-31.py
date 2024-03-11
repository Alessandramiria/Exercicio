'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. Faça um programa que implemente
uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero
deve ser informado pelo operador para indicar o final da compra. O programa
deve então mostrar o total da compra e perguntar o valor em dinheiro
que o cliente forneceu, para então calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''

# O enunciado não dá instrução sobre o momento para encerrar o programa, então coloquei um loop infinito,
# que reinicia a cada compra
while (True):
    lista_compras = {}
    total = 0
    preco_produto = 1
    n_produto = 1
    print('-' * 18)
    print('Lojas Tabajara')
    # Quando o preço do produto é colocado como '0' o programa encerra a adição de novos itens e pede o pagamento.
    # O preço é adicionado ao total, e o número do produto é incrementando em 1 a cada iteração
    while (preco_produto != 0):
      preco_produto = float(input(f'Produto {n_produto}: R$'))
      total += preco_produto
      n_produto += 1

    # Essa parte está fora do segundo loop, imprime o total, pede o valor em dinheiro
    print('Total: R${:.2f}'.format(total))
    pgto = float(input('Valor do pagamento em dinheiro: '))
    # Se o valor em real for menor que o total, solicita um novo valor
    while (pgto < total):
        print('O valor fornecido é inferior ao total das compas.')
        pgto = float(input('Valor do pagamento em dinheiro: '))
    # Calcula o troco e imprime. Após esse pedaço de código, reinicia o primeiro loop, resetando todas as variáveis.
    troco = pgto - total
    print('Troco: R${:.2f}'.format(troco))