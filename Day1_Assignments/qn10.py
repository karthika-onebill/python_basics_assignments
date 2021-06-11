# program Input : TestYantra SoftWare Solutions  output: Solutions SoftWare Testyantra
st = input("Enter the sentence  : ")
st = st.split(" ")
# using reversed() function
words = list(reversed(st))
print(" ".join(words))
# using range function
print(*[st[i] for i in range(len(st)-1, -1, -1)], sep=" ")
# using split function
print(*st[::-1])
