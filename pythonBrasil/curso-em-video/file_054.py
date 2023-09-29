''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

years = []
ages = []
maiores = 0
menores = 0

while len(years) <=3: 
	year_date = int(input('Type the year of your birth: '))
	years.append(year_date)
	if len(years) > 4:
		break

for year in years:
	agey = 2023 - year
	ages.append(agey)

for age in ages:
	if age < 18:
		menores +=1
	elif age >= 18:
		maiores +=1 

print(f'\nQuantidade de maiores de idade: {maiores}')
print(f'Quantidade de menores de idade: {menores}')
		