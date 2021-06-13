# 16) program to take dictionary from keyboard and print the sum of values.
from ast import literal_eval as lt        # using literal_eval


def printSum(dic):
    sum = 0
    for i in dic.values():
        sum += i
    return sum


dic = lt(input("Enter the values : "))      # reading input as dictionaries

print("Sum = ", printSum(dic))
