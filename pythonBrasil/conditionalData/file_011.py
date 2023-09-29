'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

sal = int(input('Salário: '))

if sal <= 280:
  aum = sal+sal*.2
  print(f'Seu salário era {sal} com o aumento de 20%, seu salário agora é {aum}')
elif 700 >= sal and sal > 280:
  aum = sal+sal*.15
  print(f'Seu salário era {sal} com o aumento de 15%, seu salário agora é {aum}')
elif 1500 >= sal and sal > 700:
  aum = sal+sal*.1
  print(f'Seu salário era {sal} com o aumento de 10%, seu salário agora é {aum}')
else:
  aum = sal+sal*.05
  print(f'Seu salário era {sal} com o aumento de 5%, seu salário agora é {aum}')
