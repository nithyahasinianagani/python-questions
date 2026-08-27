def add(x):
    x.append(1)
    return x

x=[5]
print(add(x)) #[5, 1]
print(x) #[5,1]

# predict the output,
# call by value or call by reference