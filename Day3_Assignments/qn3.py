# 3) Lambda Function to find biggest of 3 given values.

res = lambda a,b,c :"a is big -"+str(a) if a>b and a>c else "b is big -"+str(b)  if b>a and b>c else "c is big -"+str(c)
print("Biggest number is : ",res(1,2,3)) 