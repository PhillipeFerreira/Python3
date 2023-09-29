'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. '''

km = float(input('Km distance: '))

if km <= 200:
	v = km*.5
	print(f'Value: {v}')
else:
	v = km*.45
	print(f'Value: {v}')
	