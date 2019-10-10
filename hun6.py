n=int(input())
lst=list(map(int,input().split()))
lst.sort()
r=[]
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        r.append(lst[i])

if r:
    for j in set(r):
        print(j,end=" ")
        break
else:
    print("unique")         
