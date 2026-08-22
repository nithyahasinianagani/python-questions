# Accept three integers as input from the user. Print good triplet if one of the three numbers is the sum of the other two, and bad triplet otherwise.
a = int(input())
b = int(input())
c = int(input())
if a + b ==c or b + c == a or c + a == b:
    print("good triplet")
else:
    print("bad triplet")