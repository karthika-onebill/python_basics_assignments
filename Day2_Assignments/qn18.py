# 18) program to find number of occurences of each letter present in the given string

# using count() function
s = input("Enter the String : ")
s = list(s)
d = {item: s.count(item) for item in s}
print(d)
