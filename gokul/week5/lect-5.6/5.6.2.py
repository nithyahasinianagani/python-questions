#  create a recursive function to return the factorial  of a given number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


