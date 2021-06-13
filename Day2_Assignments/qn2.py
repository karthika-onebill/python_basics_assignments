''' 
2) Read an integer N . For all non-negative integers i<N , print i². See the sample for details.
            Input Format :The first and only line contains the integer,N .
            Constraints : 1≤N≤20
            Output Format : Print N lines, one corresponding to each i .
                                                                                                               Sample Input  : 5
                                                                                                               Sample Output : 0  
1
4
9
16 '''
N = int(input("Enter N : "))
if(N >= 0 and (1 <= N and N <= 20)):
    for i in range(1, N):
        if(i < N):
            print(i**2)
else:
    print("N is non-negative integer not allowed!")
