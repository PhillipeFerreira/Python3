# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

trials = 0
resp = False

while resp == False :
	num = randint(0,11)
	guest = int(input('Guess the number: '))	
	trials +=1
	if guest == num:
		print(f"\nYou won! Trials: {trials}")
		resp = True
	else:
		print(f"\nYou lost! The numeber was: {num}")
  
print(f"Your number: {guest}, PC number: {num}")
