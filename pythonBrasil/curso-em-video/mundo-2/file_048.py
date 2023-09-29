''' Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

# Variáveis acumuladoras
soma = 0
cont = 0
for x in range(1,501,2):
	if x % 3 == 0:
		soma += x
		cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')

#NOT MINE