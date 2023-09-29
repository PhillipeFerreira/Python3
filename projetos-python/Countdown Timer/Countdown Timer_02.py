#Countdown Timer 02
#Not entirely mine
import time

def countdonw(t):
	while t > 0:
		print(t)
		t -= 1
		time.sleep(1)
	print('TIME IS OVER!')
	
countdonw(10)
