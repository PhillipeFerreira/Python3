'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. '''

from random import randint

print('Guess a number from 0 to 5')
num = randint(0,5)
guest = int(input('Guess the number: '))

if guest == num:
	print('Yeah, right')
else:
	print('You missed it')

print(f'The number is {num}')
