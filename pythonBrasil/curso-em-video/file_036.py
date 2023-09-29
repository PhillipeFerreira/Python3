''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

h_v = int(input('House value: '))
sal = int(input('Salary: '))
years = int(input('How many years to pay: '))

mensal_p = (h_v)/(years*12)
sal_p = sal*.3

if mensal_p >= sal_p:
	print(f'The part you have to pay is {mensal_p}, but it is greater than 30% of your salary, {sal_p}')
	print('You cannot finnanciate this house')
else: 
	print('Coagulations, you can finnanciate ths house')
