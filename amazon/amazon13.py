"""
You are given a string ‘s’.Your task is to print the maximum length of longest palindrome present in string.

Input Description:
You are given string ‘s’

Output Description:
Print length of longest palindrome in string

Sample Input :
abcb
Sample Output :
3
"""
s=str(input())
sKey=str(input())
if sKey in s:
    print(s.index(sKey))
else:
    print(-1)

