# predict the output and explain.

x=(1,2)
y=([1,2],['a','b'])

z={x:x} 
print(z)

a={y:y}
print(a)

#{(1, 2): (1, 2)}  works because x is a tuple containing only integers Integers are hashable so the tuple is also hashable and can be used as a dictionary key
#not second one cause The tuple contains lists Lists are mutable  therefore unhashable.