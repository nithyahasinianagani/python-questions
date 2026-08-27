t=([1,2],['a','b'])
t[0]=[10,20]
print(t)

# predict the output and explain the output

#error

This means you're trying to replace the first element of the tuple.
But a tuple is immutable, so you cannot replace its elements.