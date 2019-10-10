ax=int(input())
A=list(map(int,input().split()))
c=0
lst1=[]
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        if A[i]<A[j]:
            c=c+1
            break
    else:
        lst1.append(A[i])        
print(*lst1)
print(max(A))
