# Iniciando estrutura while

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# .strip() -> Retira espaços
# .upper() -> Deixar letras maiusculas
# [0] -> Fatia string, pegando apenas primeira letra

sex = str(input('Type your sex[M/F]: ')).strip().upper()[0]

while sex not in "MmFf":
	print('Wrong input. Type M or F.')
	sex = input('Type your sex[M/F]: ').strip().upper()[0]
print(f"Sex: {sex}")
