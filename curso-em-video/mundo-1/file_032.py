'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

year = int(input('Year: '))

if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
	print('It is leap year')
else:
	print('It is not')

# NOT ENTIRE MINE