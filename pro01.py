fp=int(input())
pp=[]
for i in range(0,fp):
 lan=input()
 pp.append(lan)
thissss=[]
for i in zip(*pp):
 if(i.count(i[0])==len(i)):
  thissss.append(i[0])
 else:
  break
print(''.join(thissss))
