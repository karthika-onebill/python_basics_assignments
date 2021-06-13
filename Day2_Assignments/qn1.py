'''
1) Given an integer,n, perform the following conditional actions:
            If n is odd, print Weird
            If n is even and in the inclusive range of  2 to 5, print Not Weird
            If n is even and in the inclusive range of 6 to 10 , print Weird
            If n is even and greater than 20 , print Not Weird
                Input Format : A single line containing a positive integer,n .
                Constraints : 1≤n≤100
                Output Format : Print Weird if the number is weird; otherwise, print Not Weird. '''

# way1 (using ternery operator)
n = int(input("Enter n : "))
if(n >= 1 and n <= 100):
    print("Weird" if(n % 2 == 1) else "Not Weird" if (n % 2 == 0 and (n in range(2, 6))) else "Weird" if ((n %
          2 == 0) and (n in range(6, 11))) else "Not Weird" if (n % 2 == 0 and n > 20) else "")

# way2 (using nested if)

if(n >= 1 and n <= 100):
    if(n % 2 == 1):
        print("weird")
    if(n % 2 == 0 and (n in range(2, 6))):
        print("Not Weird")
    if(n % 2 == 0 and (n in range(6, 11))):
        print("Weird")
    if(n % 2 == 0 and n > 20):
        print("Not Weird")
