from itertools import permutations
s=input()
n=permutations(s)
for i in list(n):
    print("".join(i))
