print('Turno: (M): Manhã, (T): Tarde, (V): Vespetino')
turno = input('Qual turno você estuda? ')
turnos = ['M', 'T', 'V']

if turno == 'M':
	print('Bom dia')
elif turno == 'T':
	print('Boa tarde')
elif turno == 'V':
	print('Boa noite')
elif turno != turnos:
	print('Valor inválido. ')
