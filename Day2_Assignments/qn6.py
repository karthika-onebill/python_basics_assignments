'''
6)You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
           Input Format : The first line contains a string consisting of space separated words.
           Output Format :Print the formatted string as explained above.
            Sample Input :this is a string   
          Sample Output :this-is-a-string

          '''

# way 1 - using replace() function
s = input("Enter the String : ")
print(s.replace(" ", "-"))

# way 2 - using split and list indexing method

s = [x for x in input("Enter the string : ").split(" ")]

print(*s, sep="-", end="")

# way 3 - using manual coding

s = input("Enter the string : ")
temp_list = list(s)
for i in range(0, len(s)):
    if(s[i].isspace()):
        temp_list[i] = "-"
print(*temp_list, sep="")
