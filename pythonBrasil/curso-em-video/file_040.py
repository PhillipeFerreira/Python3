''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

nota_1 = float(input('Nota 01: '))
nota_2 = float(input('Nota 02: '))

med = (nota_1+nota_2)/2
print('A média foi: {:.1f}'.format(med))
if med < 5:
	print('REPROVADO')

elif med == 5 or med <=6.9:
	print('RECUPERAÇÃO')

else:
	print('APROVADO')
