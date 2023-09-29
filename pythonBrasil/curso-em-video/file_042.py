'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

# Verificando se é um triângulo

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

# Verificando o tipo do triângulo

if a == b and b == c:
	print('É EQUIÁTERO')
elif a == b and a == b or a == c:
	print('É ISÓSCELES')
else:
	print('É ESCALENO')

# != É O MESMO QUE 'DIFERENTE DE'
