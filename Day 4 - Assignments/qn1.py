
# decorators : To check the constrainst (if n is negative throw msg)
def checkConstraints(func) :
    def inner(st,n) :
        if(n<0) :
            print("Please provide a positive number")
        else :
            func(st,n)
    return inner

        
@checkConstraints
def display(st,n) :
    print("#OUTPUT :")
    for i in range(n) :
         print(st)

st = input("What do you want to print? ")
n = int(input("How many times do you want to print the statements? "))
display(st,n)