a=int(input())
b=[int(i) for i in input().split()]
x=0
for i in range(a):
   for j in range(i):
      if b[j]<b[i]:
         x+=b[j]
print(x)
