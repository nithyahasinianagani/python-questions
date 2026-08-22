# Accept a two digit number as input and print the sum of its digits. What about a three digit number?

n = int(input())
print(n // 10 + n % 10)

n = int(input())
print(n // 100 + (n //10)%10 + n % 10)