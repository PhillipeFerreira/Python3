#Password Generator
import random

data = [1, 2, 3, 'k', '@', 0]
pw = []

pw.append(random.choice(data))
pw.append(random.choice(data))
pw.append(random.choice(data))
pw.append(random.choice(data))
pw.append(random.choice(data))
pw.append(random.choice(data))
pw.append(random.choice(data))
pw.append(random.choice(data))

#print(*pw, sep="")
print('Your password is', *pw, sep="")
