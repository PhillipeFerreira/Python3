def lines():
    print('----'*10)

num_1 = int(input('Type the first value: '))
num_2 = int(input('Type the second value: '))
ans = 0

#for ans in range(0, 6):
while ans !=5:
    lines()
    print('''[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')
    lines()
    ans = int(input('What is the option? '))
    if ans == 1:
        sum = num_1+num_2
        lines()
        print(f'The sum is: {sum}')
        lines()
    elif ans == 2:
        mult = num_1*num_2
        lines()
        print(f'The multiplication is: {mult}')
        lines()
    elif ans == 3:
        if num_1>num_2:
            lines()
            print(f'The greater is: {num_1}')
            print(f'The ligher is: {num_2}')
            lines()
        elif num_1<num_2:
            lines()
            print(f'The greater is: {num_2}')
            print(f'The ligher is: {num_1}')
            lines()
        else: 
            lines()
            print(f'{num_1} and {num_2} are equal')
            lines()
    elif ans == 4:
        lines()
        num_1 = int(input('Type the first value: '))
        num_2 = int(input('Type the second value: '))
        lines()
    else: 
        keep = False
lines()
print('Thanks for using our software!')
