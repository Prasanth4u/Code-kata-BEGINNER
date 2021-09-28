"""
Sample Input :
7
10 7 9 3 2 1 15
Sample Output :
7 3 3 2 1 -1 -1
"""

n=int(input())
listt=[]
nNum=list(map(int,input().strip().split()))[:n]
for i in range(1,len(nNum)):
    for j in range(1,len(nNum)):
        if(nNum[i-1]>nNum[j]):
            listt.append(nNum[i])
        else:
            break
    
        
for i in listt:
    print(i)
