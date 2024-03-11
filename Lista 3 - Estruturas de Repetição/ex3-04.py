'''
Supondo que a população de um país "A" seja da ordem de 80.000 habitantes com uma taxa anual
de crescimento de 3% e que a população de "B" seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a
população do país "A" ultrapasse ou iguale a população do país "B", mantidas as taxas de crescimento.
'''

# Estabelece as variáveis informadas
pop_a = 80000
c_a = 0.03
pop_b = 200000
c_b = 0.015
anos = 0

# Incrementa a população ano a ano
while (pop_a < pop_b):
    pop_a = int(pop_a * (1 + c_a))
    pop_b = int(pop_b * (1 + c_b))
    anos += 1

print(f'Levara {anos} anos até a populção do país "A" ser superior a população do país "B"')
