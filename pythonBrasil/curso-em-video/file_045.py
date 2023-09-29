#Crie um programa que faça o computador jogar Jokenpô com você

'''
Etapas:
1. Perguntar opção do jogador
2. Selecionar opção aleatória da IA
3. Comparar resultados
4. Mostrar resultados
*5. Perguntar se quer repetir

'''

from random import randint

# Opção do jogador
player_1 = int(input('''Pedra, Papel e Tesoura:
	[1] Pedra
	[2] Papel
	[3] Tesoura
	Com qual opção você quer jogar? '''))

# Opção da máquina
player_2 = randint(1,3)

# Mostrando os resultados
# Jogador
if player_1 == 1:
	print('Você: Pedra')
elif player_1 == 2:
	print('Você: Papel')
else:
	print('Você: Tesoura')

# Máquina
if player_2 == 1:
	print('O computador: Pedra')
elif player_2 == 2:
	print('O computador: Papel')
else:
	print('O computador: Tesoura')

# Selecionando o vencedor
if player_1 == player_2:
	print('Empate!')
elif player_1 ==1 and player_2 !=2:
	print('Você é o vencedor')
elif player_1 ==2 and player_2 !=3:
	print('Você é o vencedor')
elif player_1 ==3 and player_2 !=1:
	print('Você é o vencedor')
else:
	print('O computador é o vencedor')
