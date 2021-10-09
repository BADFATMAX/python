import random

randomList = [random.randint(0, 1000) for i in range(20)]

even = 0  # четные
odd = 0  # нечетные

for i in randomList:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(randomList)
print('Amount of odd numbers = ', odd)
print('Amount of even numbers = ', even)
