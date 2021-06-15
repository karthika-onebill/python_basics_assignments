# 7) write a program to generate 6 digit random number as OTP

from random import *
import math
t=[]
for i in range(6) :
    t.append(math.floor(random()*10))
print(*t,sep="")