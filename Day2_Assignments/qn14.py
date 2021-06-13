# 14) program to take a tuple of numbers from keyboard and print its sum and average.

t = (int(x) for x in input("Enter : ").split(" "))
t = tuple(t)
print("Sum = "+str(sum(t)))
print("Average = "+str(sum(t)/len(t)))
