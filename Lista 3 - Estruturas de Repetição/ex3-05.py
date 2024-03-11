'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''

# Primeiro While utilizado para que a operação se repita, conforme enunciado.
while True:
    # Solicita as populações e crescimento e enquanto não estiverem de acordo, informa e solicita novamente
    pop_a = int(input('Informe a população do país "A": '))
    pop_b = int(input('Informe a população do país "B": '))
    while (pop_a >= pop_b):
        print('A população do país "A" deve ser menor do que a população do país "B". Tente novamente.')
        pop_a = int(input('Informe a população do país "A": '))
        pop_b = int(input('Informe a população do país "B": '))

    c_a = float(input('Informe a taxa de crescimento (%) do país "A": '))/100
    c_b = float(input('Informe a taxa de crescimento (%) do país "B": '))/100
    while (c_a <= c_b):
        print('O crescimento da popuplação do país "A" deve ser maior do que o do país "B". Tente novamente.')
        c_a = float(input('Informe a taxa de crescimento (%) do país "A": ')) / 100
        c_b = float(input('Informe a taxa de crescimento (%) do país "B": ')) / 100

    anos = 0
    # Incrementa ano a ano a população
    while (pop_a < pop_b):
        pop_a = int(pop_a * (1 + c_a))
        pop_b = int(pop_b * (1 + c_b))
        anos += 1

    print(f'Levara {anos} anos até a populção do país "A" ser superior a população do país "B"')
