import random 
import math 

y=[]
y1=[]
n=100
for i in range(n):
    y1.append(random.random())
    y.append(random.randint(0,1))
 # cross entropy function vector
cross_entropy_function = 0
for i in range(n):
    cross_entropy_function+=(-0.01)*(y[i]*(math.log2(y1[i])) + (1-y[i])*math.log2(1-y1[i]))

print("The Cross Entropy Function is",cross_entropy_function) 
