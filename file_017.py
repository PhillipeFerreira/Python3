from math import ceil

area_pt = float(input('Área a ser pintada(m2): '))
litros = area_pt/6
latas = ceil(litros/18)
galoes = ceil(litros/3.6)

print('\nComprando apenas latas de tinta: ')
custo_1 = latas*80
print(f'Quantidade de latas: {latas}')
print(f'Custo: {custo_1}')


print('\nComprando apenas galões de tinta: ')
custo_2 = galoes*25
print(f'Quantidade de galões: {galoes}')
print(f'Custo: {custo_2}')

#Parte abaixo não funcional

print('\nComprando latas e galões de tinta: ')
custo_3 = 0
m_galao = litros - (litros)
print(f'Quantidade de latas: {latas}')
print(f'Quantidade de galões: {galoes}')
print(f'Custo: {custo_3}')

#Adicionar desperdicío/litros restantes de tinta em cada caso

