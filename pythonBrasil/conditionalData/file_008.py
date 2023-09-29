produto_1 = float(input('Preço - Produto 1: '))
produto_2 = float(input('Preço - Produto 2: '))
produto_3 = float(input('Preço - Produto 3: '))

if produto_1 < produto_2 and produto_3:
	print('Produto 1 é o mais barato. Melhor opção.')

elif produto_2 < produto_1 and produto_3:
	print('Produto 2 é o mais barato. Melhor opção.')

elif produto_3 < produto_2 and produto_1:
	print('Produto 3 é o mais barato. Melhor opção.')

else:
	print('Inválido')