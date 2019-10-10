from itertools import combinations
fp,pp=list(input().split())
k=[]
pp=int(pp)
l=combinations(fp,len(fp)-pp)
for i in l:
  k.append("".join(i))
print(min(k))
