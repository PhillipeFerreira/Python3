from random import randint

# Opção do jogador
player_1 = int(input('''Pedra, Papel e Tesoura:
	[1] Pedra
	[2] Papel
	[3] Tesoura
	Com qual opção você quer jogar? '''))

# Opção da máquina
player_2 = randint(1, 3)

# Mostrando os resultados
options = ['Pedra', 'Papel', 'Tesoura']
print(f'Você: {options[player_1 - 1]}')
print(f'O computador: {options[player_2 - 1]}')

# Selecionando o vencedor
if player_1 == player_2:
    print('Empate!')
elif (player_1 == 1 and player_2 == 3) or (player_1 == 2 and player_2 == 1) or (player_1 == 3 and player_2 == 2):
    print('Você é o vencedor')
else:
    print('O computador é o vencedor')
    