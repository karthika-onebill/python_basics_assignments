# program to merge characters of 2 strings into a single string by  taking characters alternatively.   Input : S1= "ravi" S2="teja" output: rtaevjia

st1 = "ravi"
st2 = "teja"
res = ""
# way1
for x, y in zip(st1, st2):
    res += x+y

print(res)
# way2
for i in range(0, len(st1)):
    print(st1[i]+st2[i], sep="", end="")
