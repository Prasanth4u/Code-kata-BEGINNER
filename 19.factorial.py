ms=int(input(""))
fact = 1
if ms < 0:
   print("")
elif ms == 0:
   print("1")
else:
   for i in range(1,ms + 1):
       fact = fact*i
   print(fact)
