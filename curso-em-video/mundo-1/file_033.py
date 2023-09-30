''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor '''

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))

# Greater

if num1>num2 and num2>num3:
	print(f'{num1} is greater and {num3} is the less ')
elif num2>num1 and num1>num3:
	print(f'{num2} is greater and {num3} is the less ')
elif num3>num1 and num1>num2:
	print(f'{num3} is greater and {num2} is the less ')
else:
	print('Error')

# NOT DONE YET
