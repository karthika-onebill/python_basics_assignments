# 11) program for nth fibonacci number

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