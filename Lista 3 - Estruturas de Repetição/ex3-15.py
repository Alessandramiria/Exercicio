'''
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

# Solicita o até que termo o usuário deseja ver
posicao = int(input('Até que posição desejar ir na sequência de Fibonacci? '))

# Se posição for igual a zero, retorna apenas o primeiro elemento
if posicao == 1:
    lista = [0]
    print(lista)

# Estabelece a lista com os dois primeiros elementos, soma os elementos e armazena na lista
else:
    lista = [0, 1]
    for n in range(0, posicao - 2):
        lista.append(lista[n] + lista[n+1])

    print(lista)

