'''
 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
h = m = idd_mu = idd_ma = 0
keep = "S"

while True:

	print('-'*30)
	idd = int(input('Idade: '))
	sexo = str(input('Sexo[H ou M]: ')).strip().upper()[0]
	print('-'*30)

	if sexo in "HhMm":
		if idd > 18:
			idd_ma+=1
		if sexo in "Hh":
			h +=1
		if sexo in "Mm" and  idd <20:
			m +=1
			idd_mu +=1

	keep = input('Quer continuar[Sim ou Não]? ').strip().upper()[0]
	if keep in "Nn":
		break

print('-'*30)
print(f'Maiores de 18 anos: {idd_ma}')
print(f'Total de homens: {h}')
print(f'Mulheres com mais de 20 anos: {idd_mu}')
