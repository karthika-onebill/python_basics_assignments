# 14) program to convert time from 12 hour to 24 hour format

#  s  = 10:32:15PM  => 01 => hour :(2) 34=>min :(5) 67=>secs 89 =>PM/AM  
# -1,-2 =>PM/AM   ;-3,-4 =>secs , -6,-7=>mins ,-9,-10 =>hr



def convert24to12hour(s) :
    #AM to change 12 to 00
    if s[-2:]=="AM" and s[:2]=="12" :
        return "00"+s[2:]
    # only AM 
    elif s[-2:] =="AM" :
        return s[:]
    # PM and 12 no change
    elif s[-2:]=="PM" and s[:2]=="12" :
        return s[:]
    #others to add 12 to default
    else :
        return str(int(s[:2])+12)+s[2:]
s = input("Enter time : (hh:mm:ssAM/PM) ")
print(convert24to12hour(s))