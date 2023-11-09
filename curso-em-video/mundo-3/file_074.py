# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randrange

rand = [randrange(0,5)]
print(f'Desordenados: {sorted(rand)}')
print(f'Ordenados: {sorted(rand)}')
