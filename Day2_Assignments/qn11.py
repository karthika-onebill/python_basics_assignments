'''
11)Enter Nested list and print it as matrix
    Sample Input : [[1,2,3],[4,5,6],[7,8,9]]
    Sample Output: elements in matrix style
                     1 2 3
                     4 5 6
                     7 8 9

                     '''
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in l:
    for s_item in item:
        print(s_item, sep=" ", end=" ")
    print()
