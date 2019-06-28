val=input("")
vow=['a','e','i','o','u','A','E','I','O','U']
cons=['B','T','G','H','b','t','g','h']
try:
  if val in vow:
   print("Vowel")
  elif val in cons:
   print("Consonant")
except ValueError:
   print("invalid")
