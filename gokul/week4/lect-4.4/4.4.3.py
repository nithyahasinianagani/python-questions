## Generate a list of 100 random numbers between 1 and 1000, and sort the list
##  create another list even, and add all the even numbers to this even list and print the list
## similarly create another list odd, and add all the odd numbers to this odd list and print the list

import random

numbers = [random.randint(1, 1000) for i in range(100)]

numbers.sort()

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)