'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''

# Solicita o número até onde a verificação deve seguir e
# declara a lista onde serão armezenados os números primos e o contador de divisões
n = int(input('Digite o número desejado: '))
lista_primos = []
n_divisoes = 0

# Loop que vai rodar todos o números do intervalo de 1 até o número solicitado.
for x in range(1, n + 1):
    # reseta a variável de controle a cada novo número testado
    primo = True
    # Verifica se o número é primo. Só é necessário dividir um número até a sua metade + 1.
    for i in range(2, int(((x+1) / 2) + 1)):
        n_divisoes += 1
        if (x % i == 0):
            primo = False
            break
    # Caso seja primo, armeza na listagem
    if (primo):
        lista_primos.append(x)

print(f'Foram executadas {n_divisoes} divisões')
print(f'Lista de primos no intervalo\n{lista_primos}')