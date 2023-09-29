'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, 					done
qual é o nome do homem mais velho e 		-
quantas mulheres têm menos de 20 anos.		- 
'''

import math

ages = []
older = 0
namo = 10
agecon = 0
totw = 0

for people in range(1, 3):
	name = input('Type the name: ')
	age = int(input('Type the age: '))
	sex = str(input('Type the sex(m or f): ')).strip()
	agecon += age
	ages.append(age)
	
#Média das idades
	if people == 4:
		med = (math.fsum(ages))/4
		print(f'Média: {med}')
#Homem mais velho 
	if people == 1 and sex in "Mm":
		older = age
		namo = name
	if sex in "Mm" and age >older:
		older = age
		namo = name
#Mulheres de 20 anos
	if sex in "fF" and age < 20:
		totw += 1


print(f"Older: {older}")
print(f"name: {name}") 
print(f"Total of woman: {totw}") 

