n=int(input())
nNum=list(map(int,input().strip().split()))[:n]
fs=sum(nNum[0:3])
ln=n-3
ls=sum(nNum[ln:])
if(fs==ls):
    print(1)
else:
    print(0)
