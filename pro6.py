X=int(input())
Y=list(map(int,input().split()))[:X]
a1=0
for i in range(len(Y)-2):
    for y in range(i+1,len(Y)-1):
        for z in range(y+1,len(Y)):
            if Y[i]<Y[y]<Y[z] and i<y<z:
                a1=a1+1
print(a1)
