x,y=map(str,input().split())
p=0
if len(x)>len(y):
  x,y=y,x
i=0
while i<len(x):
  p+=(ord(y[i])-ord(x[i]))
  i+=1
for i in range(i,len(y)):
  p+=ord(y[i])-ord('a')+1
print(p)
