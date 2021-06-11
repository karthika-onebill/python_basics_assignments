# program how many times  each character present in string

s = "eeaabbfksjfbbeelslss"

# using bulit-in function count
print(*[i+"-----"+str(s.count(i)) for i in s], sep=" ")

# without using built in function
temp_list = []
cnt = {}
for item in s:
    if item in temp_list:
        cnt[item] += 1
    else:
        cnt[item] = 1
print(cnt)
