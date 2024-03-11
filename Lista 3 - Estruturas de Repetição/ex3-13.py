'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

# Definindo base e expoente
base = float(input('Digite a base: '))
expoente = float(input('Digite o expoente: '))

# Definindo 'resultado' como variável acumulativa. Está definida como 1, para os casos de expoente igual a 1
resultado = 1

# Calculando a ponteciação caso o expoente seja igual a zero.
if expoente == 0:
    resultado = 1

# Calculando a ponteciação caso o expoente seja menor que zero.
elif expoente < 0:
    for n in range(0, int((expoente * -1))):
        resultado = resultado * base
        resultado = 1 / resultado

# Calculando a ponteciação caso o expoente seja maior que zero:
else:
    for n in range(0, int(expoente)):
        resultado = resultado * base

# Imprimindo resultado
print(resultado)
