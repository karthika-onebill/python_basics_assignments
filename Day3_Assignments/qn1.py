# 1)  Write a Python Function to find factorial of given number with recursion.


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)


n = int(input("Enter the limit : "))
print("Factorial of the given no : ", fact(n))
