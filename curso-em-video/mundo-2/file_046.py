'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep

for x in range(10,-1,-1):
	print(x)
	sleep(1)
print('FOGOS!!')


'''
ChatGPT's

import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("BOOM! 🎉🎆🎇")

print("Contagem regressiva para o estouro de fogos de artifício:")
countdown(10)
'''