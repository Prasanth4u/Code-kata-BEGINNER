fp=input()
pf=input()
for i in range(len(fp)):
    n1=ord(fp[i])
    r1=ord(pf[i])
    l1=((n1-96)+(r1-96))
    if(l1 > 26)and(l1%26!=0):
        l1=(((n1-96)+(r1-96))%26)+96
        print(chr(l1),end='')
    elif(l1%26==0):
        l1=122
        print(chr(l1),end='')
    else:
        l1=(((n1-96)+(r1-96))+96)
        print(chr(l1),end='')
