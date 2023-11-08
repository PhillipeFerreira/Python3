#  Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

som = 0 
while True:
	n = int(input('Type a number: '))
	if n == 999:
		break
	som +=n

print(f'The sum of numbers is: {som}')
