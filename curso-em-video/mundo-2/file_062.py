primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais !=0:
    total +=mais
    while cont <=total:
        print(f'Termo: {termo}')
        termo +=razao
        cont+=1
    print('Pausa')
    mais = int(input('Quantos termos mostrar a mais: '))
print(f'Acabou. Quantidade de termos mostrados: {total}')

# NOT MINE