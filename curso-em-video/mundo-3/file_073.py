'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

times =  ('botafogo', 'palmeiras', 'red bull bragantino', 'grêmio', 'flamengo', 'atlético-mg')

print('='*50)
print(f'Times: {times}')
print('='*50)
print(f'Os cinco primeiros times: {times[0:5]}')
print('='*50)
print(f'Os últimos 4 colocados: {times[-4:]}')
print('='*50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*50)
print(f'Posição do flamengo: {times.index("flamengo")}')
print('='*50)
