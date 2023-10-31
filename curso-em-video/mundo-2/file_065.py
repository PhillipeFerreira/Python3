# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = "S"
som = med = cont = maior = menor = 0

while resp == "S":
	num = int(input('Digite um número: '))
	resp = input('Quer continuar[S/n]? ').upper().strip()
	
	cont +=1
	som +=num

	if cont ==1:
		maior = menor = num
	else:
		if num > maior:
			maior = num 
		if num < menor:
			menor = num

med = som/cont
print('A média dos {} números digitados é: {}'.format(cont, med))
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
