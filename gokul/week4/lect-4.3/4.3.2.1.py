# will 10 be printed in the output? 
# what is the difference between range(1,10) and random.randint(1,10)
import random
for i in range(20):
    print(random.randint(1,10))

#yes
#range generates a sequence(10 exculuded) random.randint generates one random num(10 included)