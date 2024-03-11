'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera
uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

# Solicita o número até onde a verificação deve seguir,
# define a lista onde serão armezenados os números primos

n = int(input('Digite o número desejado: '))
lista_primos = []

# Loop que vai rodar todos o números do intervalo de 1 até o número solicitado.
for x in range(1, n + 1):
    # reseta a variável de controle a cada novo número testado
    primo = True
    # Verifica se o número é primo. Só é necessário dividir um número até o sua metade + 1.
    for i in range(2, int(((x+1) / 2) + 1)):
        if (x % i == 0):
            primo = False
            break
    # Caso seja primo, armeza na listagem
    if (primo):
        lista_primos.append(x)

print(f'Lista de primos no intervalo\n{lista_primos}')