'''
3)  You are given the year, and you have to write a function to check if the year is leap or not.
        Input Format : Read y, the year that needs to be checked.
        Constraints: 1900≤y≤100000
        Output Format : Boolean(True/False
        Sample Input : 1990
        Sample Output  : False
'''


def checkLeapYear(year):
    if(year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


year = int(input("Enter year : "))
if(1900 <= year and year <= 100000):
    print(checkLeapYear(year))
