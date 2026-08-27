l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()
l5=l1

print(l1==l2) #True
print(l1 is l2)  #false 
print(l1==l3)  #true
print(l1 is l3) #false
print(l1==l5) #true
print(l1 is l5) #true