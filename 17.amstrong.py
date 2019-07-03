fp = int(input(""))
sum = 0
temp = fp
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if fp == sum:
   print("yes")
else:
   print("no")
