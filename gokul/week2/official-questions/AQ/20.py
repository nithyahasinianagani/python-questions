# A three digit number is called a sandwich number if the difference between its first and last digit is equal to its middle digit. Accept a three digit number as input and print sandwich if the number is a sandwich number. Print plain if the number is not a sandwich number. For example, 123 and 853 are sandwich numbers.
a = input()
f = int(a[0])
l = int(a[2])
m = int(a[1])
if f-m==l:
    print(f"{a} is sandwich num")
else:
    print("not")