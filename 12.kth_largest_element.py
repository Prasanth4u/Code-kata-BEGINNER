fp = list(map(int,input().split()))
pf = list(map(int,input().split()))
pf.sort(reverse=True)
print(pf[fp[-1]-1])
