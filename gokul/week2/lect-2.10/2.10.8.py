# simulate a coin toss, if the random number generated is >0.5 , print 'heads' else 'tails'
import random
x = random.randint(0,1)
if x>0.5:
    print("heads")
else:
    print("tails")