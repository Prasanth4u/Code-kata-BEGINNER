p=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(0,len(lst)):
    if lst[i]%2==0 and i%2==1:
        l.append(lst[i])
    elif lst[i]%2==1 and i%2==0:
        l.append(lst[i])
print(*l,sep=' ')
