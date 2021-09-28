"""
Sample Input :
7
10 7 9 3 2 1 15
Sample Output :
7 3 3 2 1 -1 -1
"""
n=int(input())
nDigits=[int(x) for x in input().split()][:n]
outList=[]
for ptr in nDigits:
    for i in range(1,len(nDigits)):
        if(ptr>nDigits[i]):
            outList.append(nDigits[i])
            break
        else:
            for j in range(i-1,len(nDigits)-1):
                if((j+1)==len(nDigits)-1):
                        outList.append(-1)
                        
                elif(nDigits[j]>nDigits[i+1]):
                    outList.append(nDigits[i+1])
                    break
                    
                
print(outList)
