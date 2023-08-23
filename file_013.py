height = float(input('Height(m): '))

m_f = input('Male(m) or female(f)? ')

if m_f == "m":
	ideal_w = (72.7*height)-58 
	print(f'Ideal weight: {ideal_w} kg')

elif m_f == "f":
	ideal_w = (62.1*height)-44.7
	print(f'Ideal weight: {ideal_w} kg')

else:
	print('You must type (m) for male and (f) for female.')