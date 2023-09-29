''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input('Type a integer number: '))
print('''Choose one of the bases to convert:
	[1] Convert to BINARY
	[2] Convert to OCTAL
	[3] Convert to HEX
	[4] Convert to all options
	''')
op = int(input('Option: '))

if op == 1:
	print(f'{num} to BINARY is equal to: {bin(num)[2:]}')
elif op ==2 :
	print(f'{num} to OCTAL is equal to: {oct(num)[2:]}')
elif op == 3:
	print(f'{num} to HEX is equal to: {hex(num)[2:]}')
elif op ==4:
	print(f'{num} to BINARY is equal to: {bin(num)[2:]}')
	print(f'{num} to OCTAL is equal to: {oct(num)[2:]}')
	print(f'{num} to HEX is equal to: {hex(num)[2:]}')
else:
	print('Invalid input')
