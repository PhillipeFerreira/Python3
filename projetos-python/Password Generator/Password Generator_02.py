#Password Generator 02
from random import sample 
import string 

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

data = lower + upper + num + symbols
pw = sample(data, 8)

print('New password: ', *pw, sep="")
