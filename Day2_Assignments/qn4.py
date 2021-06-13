''' 
4)Given the participants' score sheet for your University Sports Day. you are required to find the runner-up score.
             You are given n scores. Store them in a list and find the score of the runner-up.
            Input Format: The first line contains n . The second line contains an array A[] of n integers each separated by a space.
            Constraints : 2≤n≤5
                                     -100≤A[i]≤100
            Output Format : Print the runner-up score.
            Sample Input : 5
                                          2 3 6 6 5
             Sample Output : 5
             '''

n = int(input("Enter limit : "))
print("Enter array elements : ")
a = []
if(2 <= n and n <= 5):
    a = [int(x) for x in input().split(" ")]

# way 1 - using set to find second runner-up
s = list(set(a))
print(s[n-2])

# way 2 - using sort() function
a.sort()
print(a[-2])

# way 3 - using manual code

max = max(a[0], a[1])
secmax = min(a[0], a[1])
for i in range(2, len(a)):
    if(a[i] > max):
        secmax = max
        max = a[i]
    elif(a[i] > secmax and max != a[i]):
        secmax = a[i]
print(secmax)
