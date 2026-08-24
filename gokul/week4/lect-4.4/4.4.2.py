## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
## findout the index of number 21 in the generated list, if the number is not present in the list print -1

import random

# Generate 1000 random numbers between 1 and 1000
numbers = [random.randint(1, 1000) for i in range(1000)]

# Sort the list
numbers.sort()

# Find the index of 21
if 21 in numbers:
    print(numbers.index(21))
else:
    print(-1)
