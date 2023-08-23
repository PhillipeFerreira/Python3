area_pt = float(input('Área a ser pintada(m2): '))
litros = area_pt/3

if litros < 18:
	print('Latas de tinta necessárias: 1')
	print(f'Custo: R${80}')
elif litros > 18:
	latas = litros/18
	custo = latas * 80
	print(f'Latas de tinta necessárias: {latas}')
	print(f'Custo: R${custo}')

#Ajustar custo para números decimais
#Ajustar arredondamento de custo e latas 
# print(f"{%.2f, a})

