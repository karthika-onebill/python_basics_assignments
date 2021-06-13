# 13) program to display unique vowels present in the given
#  word(using list and also using set intersection).

s = input("Enter the word : ")
s = list(s)
# using list
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
print(*set([x for x in s if x in vowels]))
# using set intersection
s = set(s)
vowels = set(vowels)
print(s.intersection(vowels))
