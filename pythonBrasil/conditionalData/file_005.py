nota_1 = float(input('Nota 1: ')) 
nota_2 = float(input('Nota 2: '))
media = (nota_1+nota_2)/2
print(media)

if media == 7:
	print('Aprovado')

elif media <= 7:
	print('Reprovado')	

elif media > 7:
	print('Aprovado com distinção')

else:
	print('Inválido')
