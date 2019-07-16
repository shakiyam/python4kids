import random

a = random.randrange(1, 10)
b = random.randrange(1, 10)
c = int(input(f'{a} * {b} = '))
if c == a * b:
    print('Good job!')
else:
    print('Oops!')
