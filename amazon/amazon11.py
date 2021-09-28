"""
You are provided with a string ‘s’. Your task is to reverse the string using stack Data Structure.
Input Description:
You are given a string ‘s’.
Output Description:
Print the reverse string
Sample Input :
i am jsb
Sample Output :
jsb am i
"""
s=list(map(str,(input().strip().split())))
liss=[]
s.reverse()
for rec in range(0,len(s)):
    if(rec==len(s)-1):
        print(s[rec])
    else:
        print(s[rec], end=" ")
