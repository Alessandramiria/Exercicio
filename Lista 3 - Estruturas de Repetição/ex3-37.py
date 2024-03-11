'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa
que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
no campo código. Ao encerrar o programa também deve ser informados os códigos
e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes
'''

# Estabelece as listas para armazenar as informações. Essa solução se vale do fato de que as listas são indexadas
# e portanto as informações adicionadas, ficaram em posições equivalentes nas respectivas listas.
# Ex: primeiro cliente terá seu código em codigo_cliente[0], sua altura em altura_cliente[0]
# e o peso em peso_cliente[0], o segundo cliente na posição [1] e assim sucessivamente.

codigo_cliente = []
altura_cliente = []
peso_cliente = []
cont = True

while cont:
    # Verifica se o código é 0, para continuar ou encerrar o programa
    codigo = int(input('Digite seu código: '))
    if codigo == 0:
        cont = False
    else:
        # Adiciona as informações nas respectivas listas.
        codigo_cliente.append(codigo)
        altura_cliente.append(float(input('Digite sua altura: ')))
        peso_cliente.append(float(input('Digite seu peso: ')))

# Para achar o código do cliente mais alto eu busquei o valor mais alto da lista,
# em seguida busquei seu indice na sua respectiva lista e usei o indice para encontrar o código na que ocupa a mesma
# posição na lista de códigos
print(f'O cliente {codigo_cliente[altura_cliente.index(max(altura_cliente))]} é o mais alto e mede {max(altura_cliente)}m')
print(f'O cliente {codigo_cliente[peso_cliente.index(max(peso_cliente))]} é o mais pesado com {max(peso_cliente)}kg')
print(f'A média das alturas é: {round(sum(altura_cliente) / len(altura_cliente), 2)}m')
print(f'A média dos pesos é: {round(sum(peso_cliente) / len(peso_cliente), 2)}kg')