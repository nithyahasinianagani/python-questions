# write a code to find whether the given number is prime or not

num = int(imput("enter a num:"))

if num < 2:
    print("not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")