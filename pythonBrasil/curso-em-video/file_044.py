'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros '''

valor_p = float(input('Valor do produto: '))
forma_pg = int(input('''Formas de pagamento:
	[1] – à vista dinheiro/cheque: 10% de desconto
	[2] – à vista no cartão: 5% de desconto
	[3] – em até 2x no cartão: preço formal 
	[4] – 3x ou mais no cartão: 20% de juros
	Qual a forma de pagamento escolhida? ''')) 

if forma_pg == 1:
	valor_j = valor_p*.1
	valor_f = valor_p-valor_j
	print(f'''Valor do desconto: {valor_j}
		Valor final do produto: {valor_f}''')
elif forma_pg == 2:
	valor_j = valor_p*.05
	valor_f = valor_p-valor_j
	print(f'''Valor do desconto: {valor_j}
		Valor final do produto: {valor_f}''')
elif forma_pg == 3:
	parc = int(input('Quantidade de parcelas: '))
	if parc ==1:
		print('Você está comprando à vista, ganhou 5% de desconto!')
		valor_j = valor_p*.05
		valor_f = valor_p-valor_j
		print(f'''Valor do desconto: {valor_j}
			Valor final do produto: {valor_f}''')
	elif parc ==2:
		print(f'''Não há descontos para a opção selecionada. 
			Valor do produto: {valor_p}''')
	else: 
		print('Selecione outra opção.')
elif forma_pg == 4: 
	parc = int(input('Quantidade de parcelas: '))
	if parc ==1:
		print('Você está comprando à vista, ganhou 5% de desconto!')
		valor_j = valor_p*.05
		valor_f = valor_p-valor_j
		print(f'''Valor do desconto: {valor_j}
			Valor final do produto: {valor_f}''')
	elif parc ==2:
		print(f'''Não há descontos para a opção selecionada. 
			Valor do produto: {valor_p}''')
	elif parc >=3:
		valor_j = valor_p*.2
		valor_f = valor_j+valor_p
		print(f'''Valor do acréscimo: {valor_j}
			Valor final do produto: {valor_f}''')
	else: 
		print('Selecione outra opção.')
else:
	print('Seleção incorreta. Tente novamente.')
