num_1 = float(input('Number 1:'))
num_2 = float(input('Number 2:'))
num_3 = float(input('Number 3:'))

if num_1 > num_2 and num_1 > num_3:
	print(f'{num_1} is greater' )

elif num_2 > num_1 and num_2 > num_3:
	print(f'{num_2} is greater' )

elif num_3 > num_1 and num_3 > num_2:
	print(f'{num_3} is greater' )

else:
	print(f'The numbers are the same')
