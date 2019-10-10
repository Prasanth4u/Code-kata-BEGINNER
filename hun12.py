fa=int(input())
no=input();
no=list(map(str,no.split(" ")))
no.sort()
no=no[::-1]
no="".join(map(str,no))
no=int(no)
print(no)
