# 5) program to filter only even number from the list by using filter() function? 
# (with and with out lambda function)

#without lambda function  #l = list(filter(fun/lamda,list))

def checkEven(x) :
    return True if x%2==0 else False


l = [int(x) for x in input("Enter the elements :").split(" ")]
res = list(filter(checkEven,l))
print("Even numbers : " ,res)

# with lambda function

res = list(filter(lambda x: x%2==0,l))
print("Even numbers : ",res)
