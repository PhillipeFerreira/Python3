'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

if num1>num2:
	print(f'{num1} is greater than {num2}')
elif num2>num1:
	print(f'{num2} is greater {num1}')
else:  
	print(f'{num1} is equal to {num2}')
	