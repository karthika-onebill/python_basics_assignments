# 20) Input n persons weight and find average of distinct weights.
#   ( Note : distinct weights average not an average of weights)

n = int(input("Enter n : "))
print("Enter the Weights : ")
weight = []
for i in range(0, n):
    weight.append(int(input("Enter : ")))
# using set() function to get distinict weights (unique weights)
set_weight = list(set(weight))
print("Average : ", sum(set_weight)/len(set_weight))
# without using set() function
unique_list = []
for i in weight:
    if i not in unique_list:
        unique_list.append(i)
print("Average : ", sum(unique_list)/len(unique_list))
