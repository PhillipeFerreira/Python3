v_hora = float(input('Valor da hora trabalhada: '))
h_trab = float(input('Horas trabalhadas no mês: '))

salario = v_hora*h_trab

i_renda = (salario*11)/100
inss = (salario*8)/100
sindicato = (salario*5)/100
salario_l = salario - i_renda - inss - sindicato

print(f'\n+ Salário Bruto : R${salario}')
print(f'- IR (11%) : R${i_renda}')
print(f'- INSS (8%) : R${inss}')
print(f'- Sindicato ( 5%) : R${sindicato}')
print(f'= Salário Liquido : R${salario_l}')
