# take a number as input and find the sum of numbers from 1 to that number

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum:", sum)