l=[1,2,3]
print(l) #[1,2,3]

l.append(4)
print(l) #[1,2,3,4]


l.insert(2,9)
print(l) #[1,2,9,3,4]

l.pop(1)
print(l) #[1,9,3,4]

l.remove(1)
print(l) #[9,3,4]