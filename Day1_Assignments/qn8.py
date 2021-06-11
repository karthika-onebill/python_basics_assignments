# program to check whether given sub-string present in the main string

s = input("Enter the string : ")

# using find() function
print("Substring is present " if s.find(input("Enter substring : "))
      != -1 else "Substring not present")
