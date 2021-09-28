"""
25min31sec
5
1 3 5 2
"""
n=int(input())
nDigits=[int(x) for x in input().split()][:n-1]
#print(nDigits)
fact=0
nDigits.sort()
mtList=[]
#print(nDigits)
for i in range(1,n+1):
    fact += 1
    mtList.append(fact)
#print(mtList)

    
for j in range(0,len(nDigits)+1):
    if(j==len(nDigits)):
        print(mtList[j])
        
    elif(nDigits[j]!=mtList[j]):
        print(mtList[j])
        break
    
