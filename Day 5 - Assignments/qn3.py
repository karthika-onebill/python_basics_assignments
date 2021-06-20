#for loop
def forLoop(list_var,type_var=0) :
   
    if(type_var==1) :
        sum=0
        for i in Num :
            sum+=int(i)
        print("The sum from for loop:",sum)
    else :
        for i in list_var :
            print(i)
        print()

#while loop
def whileLoop(list_var,type_var=0) :
   
    if(type_var==1) :
        sum=0
        i=0
        while(i<len(Num)) :
            sum+=int(Num[i])
            i=i+1
        print("The sum from while loop:",sum)
    else :
        i=0
        while(i<len(list_var)) :
            print(list_var[i])
            i=i+1
        print()


#list 1
numbers = [1,2,3,4,5]
#list 2
Weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#list 3
Num = ['222','100','85','500','300']

#print numbers in list 'numbers' - using for loop

forLoop(numbers)
#print numbers in list 'numbers' - using while loop
whileLoop(numbers)

#print the days of the week 'weekdays' - using for loop

forLoop(Weekdays)
#print the days of the week 'weekdays' - using while loop

whileLoop(Weekdays)


#print sum of all numbers - for loop
forLoop(Num,1)
#print sum of all numbers - for loop
whileLoop(Num,1)



