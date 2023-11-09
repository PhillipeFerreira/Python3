#  Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num_ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
'''
while True:
	num = int(input('Entre com um número entre 0 e 10: '))

	for pos, x in enumerate(num_ext):
		if  num ==pos:
			print(f'O número digitado foi {num_ext[pos]}')

	if num < 0 or num > 10:
		print('Erro. Digite novamente\n')

'''
# Maneira mais fácil
while True:
	num = int(input('Entre com um número entre 0 e 10: '))
	if num >= 0 and num <=10:
		break
print(num_ext[num])
