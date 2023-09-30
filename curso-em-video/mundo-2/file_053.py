'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
# Desconsiderando espaços
junto = ''.join(palavras)
print(junto)
#Criando inverso da frase
for letra in range(len(junto)-1,-1,-1):
	print(junto[letra])
