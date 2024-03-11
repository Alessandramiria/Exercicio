from math import ceil, floor
area = float(input('Digite o tamanho da área que desejar pintar: '))

l_necessarios = ceil((area / 6) * 1.1)
p_lata = 80.00
l_lata = 18
p_galao = 25.00
l_galao = 3.6

print(l_necessarios)
print(f'Comprando apenas latas, você usará {ceil(l_necessarios)} litros e gastará R${p_lata if (l_necessarios / l_lata) < 1 else ceil((l_necessarios / l_lata)) * p_lata }')
print(f'Comprando apenas galões, você usará {ceil(l_necessarios)} litros e gastará R${p_galao if (l_necessarios / l_galao) < 1 else ceil((l_necessarios / l_galao)) * p_galao }')

if l_necessarios <= (l_galao * 3):
    print(f'Com a combinação mais econômica você gastará {ceil(l_necessarios)} litros e gastará R${p_galao if (l_necessarios / l_galao) < 1 else ceil((l_necessarios / l_galao)) * p_galao }')
    print(f'Compre {ceil((l_necessarios % l_lata) / l_galao)} galões.')
elif l_necessarios > (l_galao * 3) and l_necessarios % l_lata > (l_galao * 3):
    gasto = (ceil((l_necessarios / l_lata)) * p_lata)
    print(f'Com a combinação mais econômica você gastará {ceil(l_necessarios)} litros e gastará R${gasto}')
    print(f'Compre {ceil((l_necessarios / l_lata))} latas.')
else:
    gasto = (floor((l_necessarios / l_lata)) * p_lata) + (ceil((l_necessarios % l_lata) / l_galao)) * p_galao
    print(f'Com a combinação mais econômica você usará {ceil(l_necessarios)} litros e gastará R${gasto}')
    print(f'Compre {floor((l_necessarios / l_lata))} latas e {ceil((l_necessarios % l_lata) / l_galao)} galões.')
