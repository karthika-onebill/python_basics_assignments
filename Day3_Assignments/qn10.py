# 10) You are given a date. Your task is to find what the day is on that date.

import datetime
inp = input("Enter date : [yyyy-mm-dd]")
l = inp.split("-")
x = datetime.datetime(int(l[0]),int(l[1]),int(l[2]))
print("Day  : ",x.strftime("%A"))
