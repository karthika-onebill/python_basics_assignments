'''
10)Read a list and sort it in reverse of default natural sorting order..(using sort(reverse=True))
   Sample Input : [20,5,16,19,4]
   Sample Output: [20,19,16,5,4]

   '''
n = int(input("Enter limit : "))
a = []
for i in range(0, n):
    a.append(int(input("Enter : ")))
a.sort(reverse=True)
print(a)
