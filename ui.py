 
import random
import time
import os

count = []
l = [1,2,3,4,5,6]
y = 0
while y <= 10:
    x = random.choice(l)
    if x == 1:
        count.append(x)
    
    y += 1

print(count)





