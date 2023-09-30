''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

s = int(input('Salary: '))

if s >=1250:
	s_a = s+s*.1
	print(s_a)
elif s <=1250:
	s_a = s+s*.15
	print(s_a)
