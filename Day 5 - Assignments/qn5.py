def checkOrder(func) :
    def inner(list_of_nos) :
        index=0
        for i in list_of_nos :
            i=int(i)    # for removing zeros (ex:09099999780=>9099999780)
            i=str(i)     
            if(i[0:2]=='91') :  # for checking country code present at first or not (+91)
                i="+"+str(i)
            else :
                i="+91"+str(i)
            
            cnt=0
            temp=''
            for j in i :
                cnt=cnt+1       
                temp+=j
                if(cnt==8) :
                    temp+=" "   #adding space between 5th digit
                if(cnt==3) : 
                    temp+=" "   # adding space after country code

            list_of_nos[index]=temp
            index=index+1

        return func(list_of_nos)
    return inner

#checkorder - decarator using to add country code at first and split spaces between each 5 digits.
@checkOrder
def findOrdering(list_of_nos) :  

    list_of_nos.sort() #sorting of numbers
    return list_of_nos


n = int(input("Total no of mobile numbers : "))                 
list_of_nos=list()
for i in range(n) :
    list_of_nos.append(input())
res = findOrdering(list_of_nos)
print()
print(*res,sep="\n",end="\n")