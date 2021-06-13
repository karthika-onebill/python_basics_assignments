'''
8) the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string

'''

# way 1 : using count() function
s = input("Enter the string : ")
substring = input("Enter the substring : ")
print(s.count(substring))

# way 2 : without using count()
cnt = 0
for i in range(len(s)):
    if(substring == s[i:i+len(substring)]):
        cnt += 1
print(cnt)
