# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

typed = som = 0
num = int(input('Digite um número[999: PARAR]: '))

while num != 999:
	som +=num
	typed +=1
	num = int(input('Digite um número[999: PARAR]: '))

print('Soma dos {} números digitados: {}'.format(typed, som))
s