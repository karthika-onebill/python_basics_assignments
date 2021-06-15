# 9) Given a list of rational numbers,find their product.
from functools import *
from fractions import *
def product(frac) :
    res = Fraction(reduce(lambda x,y:x*y,frac))
    return res.numerator,res.denominator
n = int(input("Enter limit : "))
frac =[]
for i in range(n) :
    frac.append(Fraction(*map(int,input("Enter : ").split())))
res = product(frac)
print(res)


