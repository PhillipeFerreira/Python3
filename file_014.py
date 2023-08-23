p_kg = float(input('Quantidade de peixe(kg): '))

if p_kg > 50:
	multa = (p_kg -50)*4
	print(f'Quantidade excendente {p_kg-50}kg.')
	print('Valor da multa(R$): ',multa)
elif p_kg < 50:
	print('Não houve multa aplicada. Quantidade abixo de 50kg.')
elif p_kg == 50: 
	print('Não houve multa aplicada. Quantidade no limite permitido.')

