fp=input()
fa=0
ms=[]
for i in range(0,len(fp)-1):
    for j in range(i+1,len(fp)):
        k=fp[i:j+1]
        l=k[::-1]
        if k==l:
            ms.append(len(fp)-len(l))
print(min(ms))
