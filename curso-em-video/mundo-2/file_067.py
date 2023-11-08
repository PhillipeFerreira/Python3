#  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

cont = 0
while True: 
	num = int(input('Type a number to get its multiplication table: '))
	if num < 0:
		print('Negative numbers are not allowed.')
		break
	print('-'*20)
	for x in range(1,11):
		tab = num * x
		print(f'Table: {num} x {x}: {tab}')
	print('-'*20)

