'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

h = 0
l = 0

for w in range(1, 6):
	weight = float(input(f'Type the weight {w}: '))
	if w == 1:
		h = weight
		l = weight
	else:
		if weight > h:
			h = weight
		if  weight < l:
			l = weight
print(f'''\nHeavier: {h} kg
Lighter: {l} kg''')
