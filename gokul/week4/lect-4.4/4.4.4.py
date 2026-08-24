## generate a list of 15 numbers random numbers from 1 to 15 and sort it
## print all the numbers from 1 to 15 , which are not in the generated list

import random

numbers = [random.randint(1, 15) for i in range(15)]

numbers.sort()

print("Generated list:", numbers)

for num in range(1, 16):
    if num not in numbers:
        print(num)