## write a python code to print the maximum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]



maximum = l[0]

for num in l:
    if num > maximum:
        maximum = num

print(maximum)