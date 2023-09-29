''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input(' Digite um número: '))
tot = 0
for x in range(1, num+1):
	if num % x ==0:
		tot += 1
		print('\033[33m', end=' ')
	else:
		print('\033[31m', end=' ')
	print(f'{x}',end='')
	print(f'Total de números divisíveis: {tot}')
 