import random

a = random.randrange(1, 10)
b = random.randrange(1, 10)
c = input(f'{a} * {b} = ')
if int(c) == a * b:
    print('Good job!')
else:
    print('Oops!')
