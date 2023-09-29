#Countdown Timer 01
import time

print('Welcome to Countdown Timer!')
t = int(input('Time: '))
#t = 10

while t > 0:
	print(t)
	t -= 1
	time.sleep(1)
print('TIME IS OVER!')
