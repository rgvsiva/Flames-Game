def length(b, g):
    for i in b:
        if i in g:
            b.remove(i)
            g.remove(i)
            return length(b, g)
    le = len(g) + len(b)
    return le
# -------------------------------------------
def remspc(s):
    lis = []
    for i in s.lower():
        if i.isalpha():
            lis.append(i)
    return lis
# --------------------------------------------
def final(n,f):
    if len(f)==1:
        return f
    else:
        v=n%len(f)
        if v==0:
            return final(n,f=f[:-1])
        else:
            return final(n,f = f[v:] + f[:v-1])
#------------------------------------
#*****************FLAMES******************#
#from logic import *
print("*************----FLAMES----**************")
b=input("Enter Boy's Name: ")
g=input("Enter Girl's Name: ")
boy=remspc(b)
girl=remspc(g)
#print(boy,girl)
count=length(boy,girl)
fm=['Friend','Lover','Attraction','Marriege','Enemy','Sister']
fin=final(count,fm)
print ('Result:',fin[0])
