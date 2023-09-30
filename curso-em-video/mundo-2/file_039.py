'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

age_y = int(input('Ano de nascimento: '))
age_num =2023 - age_y

if age_num == 18:
	print('Está na hora de se alistar! Seu alistamento é nesse ano, 2023')

elif age_num > 18:
	time_a = age_num - 18
	year_a = 2023 - time_a
	print(f'Você passou {time_a} anos do prazo para se alistar')
	print(f'Seu ano de alistamento foi em {year_a}')

elif age_num < 18:
	time_l = 18 - age_num
	year_a = 2023 + time_l
	print(f'Faltam {time_l} anos para você se alistar.')
	print(f'Seu ano de alistamento será em {year_a}')
else:
	print('Error')   
'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
	print('Você tem que se alistar IMEDIATAMENTE')

elif idade < 18:
	tempo = 18 - idade 
	print(f'Ainda faltam {tempo} anos para o alistamento')

elif idade > 18:
	tempo =idade - 18
	print(f'Você já deveria ter se alistado há {tempo} anos')
'''