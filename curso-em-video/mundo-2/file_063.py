n = int(input("Veja se um número é primo: "))
cont = 0
i = 0

while i <= n or cont < 2:
    i = i + 1
    x = n % i
    if x == 0:
        cont = cont + 1
    else:# para quando entra com o numero 1
        print('Não é primo')
        break

if cont <= 2 and n !=1:
    print("É primo")
else:

    print("Não é primo")