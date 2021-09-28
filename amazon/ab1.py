st=list(map(str,input().strip().split()))
s=st[0]
p=int (st[1])
    
s1=[]
s1[:1]=s

if(p>0):
    for i in range(p-1,len(s1),p):
        s1[i] = s1[i].upper()
    for i in s1:
        print(i, end="")
else:
    print(s)
