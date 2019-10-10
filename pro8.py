import math
n,m=map(int,input().split())
a=[]
b=list(map(int,input().split()))
for i in range(0,m):
    x,y=map(int,input().split())
    a.append([x,y])
for i in a:
    d=i[0]-1
    e=i[1]-1
    print(math.gcd(b[d],b[e]))
