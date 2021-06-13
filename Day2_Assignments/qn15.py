# 15) program to eleminate duplicates present in the list? (with and without using set function)
l = [x for x in input("Enter list : ").split(" ")]
# using set function
print(set(l))
# without using set function
temp_list = []
for i in l:
    if i in temp_list:
        l.remove(i)
    elif i not in temp_list:
        temp_list.append(i)
print(temp_list)
