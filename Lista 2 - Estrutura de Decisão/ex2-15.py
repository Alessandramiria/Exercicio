'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)

p_segmento = float(input('Primeiro segmento: '))
s_segmento = float(input('Segundo segmento: '))
t_segmento = float(input('Terceiro segmento: '))

if p_segmento < (s_segmento + t_segmento) and s_segmento < (p_segmento + t_segmento) and t_segmento < (p_segmento + s_segmento):
    print('O três segmentos acima podem formar um triângulo!')


    if p_segmento == s_segmento == t_segmento:
        print('E o triângulo é equilatero.')
    elif p_segmento == s_segmento or p_segmento == t_segmento or s_segmento == t_segmento:
        print('E o triângulo é isóceles.')
    elif p_segmento != s_segmento != t_segmento:
        print('E o triângulo é escaleno.')
else:
    print('O três segmentos acima não podem formar um triângulo!')