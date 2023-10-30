# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <=10:
    print(f'Termo: {termo}')
    termo +=razao
    cont+=1
print('Acabou')

# NOT MINE
        