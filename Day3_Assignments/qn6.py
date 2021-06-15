# 6) program to print sum of elements of the list  using reduce() function

# syntax for reduce : list(reduce(fun/lamda,list))

from functools import *

l =[int(x) for x in input("Enter the elements : ").split(" ")]

res = reduce(lambda x,y: x+y,l)    # using lamda function
print("Sum of elements : ",res)


def checkSum(x,y) :           # without using lambda function
    return x+y

res = reduce(checkSum,l)
print("Sum of elements : ",res)