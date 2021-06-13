'''

12) Using List Comprehension 
       a) print powers of 2 in  range(1,10)
       b) print squares in range(1,15)
       c) print double of number in range (1,40) and number should be even  '''

# print powers of 2 in range(1,10)
a = [i**2 for i in range(1, 10)]
print(*a, sep=" ")
# print squares in range(1,15)
b = [i**2 for i in range(1, 15)]
print(*b, sep=" ")
# print double of number in range(1,40) and number should be even

c = [i*2 for i in range(1, 40) if i % 2 == 0]
print(*c, sep=" ")
