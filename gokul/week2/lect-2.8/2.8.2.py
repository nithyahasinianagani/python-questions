# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB

a = int(input("YOB:"))
b = 2026-a 
print(b)

if b>=18:
    print("eligible")
else:
    print("not eligible")