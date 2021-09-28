"""
4
2 4 4 4
"""

n=int(input())
digits=[int(x) for x in input().split()]
sList=[]
lList=[]
fact=0


for i in digits:
    fact += i
    sList.append(fact)

#print(sList)

for i in range(0,len(sList)):
    if(sList[i]%2==0):
        lList.append(sList[i])
    else:
        lList.append(digits[i])

for j in range(0,len(lList)):
    if((len(lList)-1)==j):
        print(lList[j])
    else:
        print(lList[j], end=" ")
