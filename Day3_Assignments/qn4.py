# 4) program to generate fibonacci series


# using def return normal function
def fibanocci(n) :
    temp=[]
    a=0
    b=1
    temp.append(a)
    temp.append(b)
    while(a+b<n) :
        a,b = b,a+b
        temp.append(b)
    return temp

n = int(input("Enter the limit : "))
print(fibanocci(n))

#using generators

def fib() :
    a,b=0,1
    while True :
        yield a
        a,b = b,a+b
for f in fib() :
    if f>n :
        break
    print(f)