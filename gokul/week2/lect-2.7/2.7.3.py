# predict the output


alpha="abcdefghijklmnopqrstuvwxyz"
i=24


print(alpha[i+1]) #25 so......z
print(alpha[i+2])#indexerror.....so doesnt excecute furthur code
print(alpha[i+2]%26)#error math op cant be done on index
print(alpha[(i+2)%26])#a