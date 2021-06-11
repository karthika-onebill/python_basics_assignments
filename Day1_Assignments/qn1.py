# Read 3 numbers and print max value using ternary operator . (don’t use pre defined functions)
a, b, c = [int(x) for x in input("Enter : ").split(" ")]
print(a if a > b and a > c else b if b > a and b > c else c)
