# 8) program to generate random password of length 6 where 1st 3rd 5th are alphabet symbols
#  2nd 4rth 6th are digits (like a3b5d6)

from random import *
import math
import string         #using string package to generate random password
t=[]
for i in range(6) :
    if i%2==0 :
        #t.append(math.floor(random()*10))
        t.append(choice(string.digits))
    elif i%2==1 :
        t.append(choice(string.ascii_lowercase))
print("Password : ",*t,sep="")