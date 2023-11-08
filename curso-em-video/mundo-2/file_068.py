# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

while True:
	player_o = input('\nEscolha ímpar[I] or par[P]: ').upper().strip()
	if player_o in "Pp":
		ai = "P"
	if player_o in "Ii":
		ai = "P"

	p_num = int(input('Qual o número? '))
	opt = randint(0, 10)
	soma = p_num + opt

	if (player_o in "Pp") and (soma%2 == 0):
		print('-'*20)
		print(f'A soma é: {soma}')
		print(f'É par. Você venceu!\n')
		print(f'Seu número: {p_num}')
		print(f'Número do computador: {opt}')
		print('-'*20)

	elif (player_o in "Ii") and (soma%2 != 0):
		print('-'*20)
		print(f'A soma é: {soma}')
		print(f'É ímpar. Você venceu!\n')
		print(f'Seu número: {p_num}')
		print(f'Número do computador: {opt}')
		print('-'*20)
		break

	else: 
		print('-'*20)
		print(f'Você perdeu')
		print(f'Soma: {soma}')
		print('-'*20)
		break
