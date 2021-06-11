# program for sum of first n numbers
n = int(input("Enter the limit : "))
print("---------Predefined function-----------")
print(sum([int(x) for x in range(0, n+1)]))
print("--------without predefined function----------")
sum = 0
for i in range(0, n+1):
    sum += i
print(sum)
