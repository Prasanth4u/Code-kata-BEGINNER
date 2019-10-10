n=list(map(str,input().split()))
lst=[]
for i in n:
	s=i[::-1]
	lst.append(s)
for j in lst:
	print(j,end=" ")
