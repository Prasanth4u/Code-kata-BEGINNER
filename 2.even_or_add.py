val = input ("")
try:
   val = int(val)
   mod = val% 2
   if mod > 0:
    print("Odd")
   else:
    print("Even")
except ValueError:
   print("invalid")
