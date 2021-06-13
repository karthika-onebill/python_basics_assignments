# 17) program to accept student name and marks from keyboard and create a dictionary .
# Also display student marks by taking student name as input
n = int(input("Enter limit : "))
for i in range(n):
    s_name = input("Enter student name : ")
    dic = {s_name: [marks for marks in input("Enter marks :").split(" ")]}
check_name = input("Enter name to get marks : ")
print("--------Student Marks---------")
print(dic[check_name])
