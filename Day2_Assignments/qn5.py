''' 
5) given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
     Like Pythonist 2  to pYTHONIST 2.  '''

# using swapcase() method
s = input("Enter string : ")
print(s.swapcase())

# using manual coding
s = list(s)
for i in range(0, len(s)):
    if s[i].isupper():
        s[i] = s[i].lower()
    elif s[i].islower():
        s[i] = s[i].upper()
print(*s, sep="")
