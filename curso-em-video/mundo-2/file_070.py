'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''
total = bart = m_mil = 0

while True:
	print('-'*30)
	prod = input('Nome do produto: ')
	price = float(input('Preço do produto: '))
	print('-'*30)

	total += price

	if price > 1000:
		m_mil +=1

	if price < bart:
		bart = prod
	elif bart == 0: 
		bart = price

	keep = input('Quer continuar[Sim ou Não]? ').upper().strip()[0]
	if keep in "Nn":
		break

print('-'*30)
print(f'Total gasto na compra: {total}')
print(f'Produtos que custam mais de $1000: {m_mil}')
print(f'Produto mais barato: {bart}')
