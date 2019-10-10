n=input()
k1=1
for j in range(len(n)-1):
    s=n[j]+n[j+1]
    p=int(s)
    if p<=26 and n[j]!="0":
        k1+=1
if k1==3:
    print(k1)
else:
    print(k1+(k1-1)//2)
