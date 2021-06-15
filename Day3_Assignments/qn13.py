# 13) Given a dictionary and a character array, print all valid words that are possible
#  using characters from the array.
def charoccur(i) :
    d={}
    for j in i :
        d[j]=i.count(j)
    return d

def checkValidPairs(dic,char_pairs) :
    for i in dic :
        flag =1
        chars = charoccur(i)
        for k in chars :
            if k not in char_pairs :
                flag=0
            else :
                if(char_pairs.count(k)!=chars[k]) :
                    flag=0
        if flag==1 :
            print(i)

            
dic = {'me','man','go','eat'}
char_pairs = ['m','a','e','t','g','o']
checkValidPairs(dic,char_pairs)