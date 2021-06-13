'''

9)You are given a string S.Your task is to find out
  if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
  Input Format : A single line containing a string S .
  Constraints : 0 ≤ len(S) ≤1000
  Output Format:
       In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
      In the second line, print True if  has any alphabetical characters. Otherwise, print False.
      In the third line, print True if  has any digits. Otherwise, print False.
      In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
      In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
 Sample Input : qA2
  Sample Output :
                                  True
                                  True
                                  True
                                  True
                                  True

                                  '''


def checkFunctionality(fun):
    status = False
    for i in s:

        if fun(i):
            status = True

    return status


s = input("Enter the String : ")
if(0 <= len(s) and len(s) <= 1000):
    print("True" if s.isalnum() else "False")
    print(checkFunctionality(str.isalpha))
    print(checkFunctionality(str.isdigit))
    print(checkFunctionality(str.isupper))
    print(checkFunctionality(str.islower))
