# program Input: a4k3b2  Output:aeknbd (ie  After a 4rth character e ..after k 3rd character n after b 2nd character d)

st = "a4k3b2"
res = ""
for i in range(0, len(st)):
    if(st[i].isdigit()):
        res += st[i-1]+(chr(ord(st[i-1])+int(st[i])))
print(res)
