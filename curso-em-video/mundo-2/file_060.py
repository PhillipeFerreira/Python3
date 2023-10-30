# Calcular o fatorial de um número

num = int(input('Type the number: '))
verif = num
f = 1
while verif > 0:
    print(f'{verif}', end='')
    print('x' if verif > 1 else '=', end='')
    
    f *=verif
    verif -=1
print(f)
