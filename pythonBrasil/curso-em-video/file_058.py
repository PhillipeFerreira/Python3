# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Prompt do desafio 28:
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 

'''
from random import randint

print('Guess a number from 0 to 5')
num = randint(0,5)
guest = int(input('Guess the number: '))

if guest == num:
	print('Yeah, right')
else:
	print('You missed it')

print(f'The number is {num}')

'''

from random import randint

trials = 0
num = randint(0,5)
#guest = int(input('Guess the number: '))
guest = -1

while guest != num:
	#print('Missed. Try again.')
	guest = int(input('Guess the number: '))	
	trials +=1

print(f"You won! Trials: {trials}")
print(f"Your number: {guest}, PC number: {num}")
