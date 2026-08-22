# Accept three non-negative real numbers as input from the user. If the three numbers form the sides of a triangle, print True . If not, print False.
a = int(input())
b = int(input())
c = int(input())
print(a**2 + b**2 == c **2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2)
    