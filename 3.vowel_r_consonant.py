val=input("")
vow=['a','e','i','o','u','A','E','I','O','U']
cons=['z','Z','B','T','G','H','b','t','g','h','f','F']
try:
  if val in vow:
   print("Vowel")
  elif val in cons:
   print("Consonant")
  else:
   print("invalid")
except ValueError:
   print("invalid")
