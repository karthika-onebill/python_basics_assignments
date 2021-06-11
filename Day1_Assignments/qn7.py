# Reverse Word  by Word  Input: Test Yantra    Output: tseT artnaY

s = "Test Yantra"
l = s.split(" ")
print("".join([i[::-1]+" " for i in l]))  # using slice operator


# without using slice operator
for i in l:
    t = ""
    for j in range(len(i)-1, -1, -1):
        t += ""+i[j]
    print(t, sep=" ", end=" ")
