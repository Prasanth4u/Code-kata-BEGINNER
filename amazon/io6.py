"""
Sample Input :
2 5
2 5 6
2 4 5
Sample Output :
2 5
2 5 6
2 4 5
"""
n=list(map(int,input().strip().split()))
sec=list(map(int,input().strip().split()))
thir=list(map(int,input().strip().split()))

nl=len(n)
sl=len(sec)
tl=len(thir)

lastN=n[nl-1]
lastSec=sec[sl-1]
lastThir=thir[tl-1]

for i in n:
    if(i==lastN):
        print(i)
    else:
        print(i, end=" ")
for j in sec:
    if(j==lastSec):
        print(j)
    else:
        print(j, end=" ")
for k in thir:
    if(k==lastThir):
        print(k)
    else:
        print(k, end=" ")
