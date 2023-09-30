''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if (b - c) < a < (b+c):
	print('Primeira condição satisfeita') 
else: 
	print('Não pode formar um triângulo')
if (a - c) < b < (a+c):
	print('Segunda condição satisfeita')
else: 
	print('Não pode formar um triângulo')
if (a - b) < c < (a+b):
	print('Terceira condição satisfeita') 
	print('É um triângulo')
else: 
	print('Não pode formar um triângulo')
