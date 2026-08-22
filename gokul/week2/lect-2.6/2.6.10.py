# use of index menthod

# predict the output

x="python is a programming language. python is easy to learn.I love pykkara false"

print(x.index("python",10))
print(x.index("python",0,10))
print(x.index("python",10,20))

#searches for python starting from index 10 it occures at 34
#searches occurance of python between 0 and 10 the firat occurance is at 0 so prints 0\
#there is no python between 10 and 20