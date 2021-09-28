"""
Given 2 strings S1 and S2. Find if String2 is substring of String1. If it is print the index of the first occurrence. else print -1.
Input Size : 1<= N <= 100000
Sample Testcases :
1)INPUT
test123string
123
OUTPUT
4
"""
s=str(input())
sKey=str(input())
if sKey in s:
    print(s.index(sKey))
else:
    print(-1)

