# program to remove duplicate characters of the string      Input : mississippi   Output:misp
from collections import OrderedDict as od
s = "mississippi"

print("".join(set(s)))  # using set to remove duplicates without order

# using ordered dict to remove duplicates with order
print("".join(od.fromkeys(s)))

# using sorted function to remove duplicates with order
print("".join(sorted(set(s), key=s.index)))

# using manual logic
temp_list = []
for i in s:
    if i not in temp_list:
        temp_list.append(i)
print(*temp_list, sep="")
