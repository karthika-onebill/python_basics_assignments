'''

7) Read a given string, change the character at a given index and then print the modified string.
  Input Format :The first line contains a string,S.
                The next line contains an integer i, denoting the index location and a character c separated by a space.
  Output Format: Using any of the methods explained above, replace the character at index i with character c .
  Sample Input : abracadabra
                                5 k
  Sample Output : abrackdabra

  '''

s = input("Enter the string : ")
index = int(input("Enter the index to be update : "))
value = input("Enter the character to be update : ")
s = list(s)
s[index] = value                   # for changing value
print(*s, sep="")
