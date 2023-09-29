'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''


list1 =[]
while len(list1)<=6:
	num = int(input('Número: '))
	list1.append(num)

for x in list1:
	if x %2 == 0:
		x +=x
		print(f'A soma dos números pares é: {x}')
		
#NOT MINE

soma = 0
cont = 0

for x in range(1,7):
	num = int(input('Número: '))
	if num %2 ==0:
		soma += num
		cont += 1
print(f'''
	Quantidade de pares: {cont}
	Soma dos pares: {soma}''')
