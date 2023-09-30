import random
# Welcome to PyBingo!

random_choices = []
ur_sheet = []
pc_sheet = []

ur_ones = []
ur_ones_notRepeated = []
pc_ones = []
pc_ones_notRepeated = []

# Generating a random number sheet for the player 
for y in range(5):
    n1 = random.randint(1, 30)
    ur_sheet.append(n1)

# Generating a random number sheet for the computer 
for z in range(5):
    n2 = random.randint(1, 30)
    pc_sheet.append(n2)

# Generating random number to compare with sheets
for num in range(50): # 50 is the size of the list
    n = random.randint(1, 50)
    random_choices.append(n)
    size = len(random_choices)

print('Welcome to PyBingo!\n\n')
print(f'Your number sheet is: {ur_sheet}')
print(f'Computer number sheet is: {pc_sheet}\n')

# Checking numbers with number sheets
for x in random_choices:
    if x in ur_sheet:
        ur_ones.append(x)

    if x in pc_sheet:
        pc_ones.append(x)

# Removing repeated elements
# Player
for element in ur_ones:
    if element not in ur_ones_notRepeated:
        ur_ones_notRepeated.append(element)
        print(f'You got {element}!')

# Removing repeated elements
# Computer
for element in pc_ones:
    if element not in pc_ones_notRepeated:
        pc_ones_notRepeated.append(element)
        print(f'Computer got {element}!')

size_ur_ones_notRepeated = len(ur_ones_notRepeated)
size_pc_ones_notRepeated = len(pc_ones_notRepeated)

size_ur_sheet = len(ur_sheet)
size_pc_sheet = len(pc_sheet)

# Victory conditions
if size_ur_sheet == size_ur_ones_notRepeated:
    print(f'\nYou won!')

elif size_pc_ones_notRepeated == size_pc_sheet:
    print('\nComputer won!')

else: 
    print('\nNo one won...')

# Printing drawn numbers
if size == 50:
    print(f'\n\nThe numbers drawn were: {random_choices}\n')
