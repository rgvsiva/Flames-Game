#*****************FLAMES******************#
from logic import *
print("*************----FLAMES----**************")
b=input("Enter Boy's Name: ")
g=input("Enter Girl's Name: ")
boy = remspc(b)
girl = remspc(g)

count=length(boy,girl)
fm=list('flames')
fin=final(count,fm)

flames={'f':'Friend','l':'Lover','a':'Attraction','m':'Marriage','e':'Enemy','s':'Sister'}
result=(flames[fin[0]])
print ('Result: ',g.capitalize(),' is "',result,'" for ',b.capitalize(),'.')