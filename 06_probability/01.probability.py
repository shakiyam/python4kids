import random

frequency = [0, 0, 0, 0, 0, 0]
for c in range(100):
    r = random.randrange(1, 7)
    frequency[r - 1] += 1
for i in range(1, 7):
    print(f'{ i }: { frequency[i - 1] }')
