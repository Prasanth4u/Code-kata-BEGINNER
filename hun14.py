e=input()
v=input()
v=v.split()
for l in v:
    if v.count(l)==1:
        print(l)
        break
