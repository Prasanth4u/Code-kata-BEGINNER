n=int(input(""))
N=list(map(int,input().strip().split()))[:n]
N.sort()
for b in N:
    print(b,end=" ")
