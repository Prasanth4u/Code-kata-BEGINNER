n= int(input())
FullNum= list(map(int,input().strip().split()))[:n]
c= int(input())
gNum= list(map(int,input().strip().split()))[:c]

for x in gNum:
    if x in FullNum:
        occ=FullNum.count(x)
        print(occ, end=' ')
    else:
        print("Not Present", end=' ')

#########QUESTION#######
"""
Shreya is a brilliant girl. She likes to memorize the numbers.
These numbers will be shown to her. As an examiner develop an algorithm to test her memory.

CONSTRAINTS
1<=Y,N,T<=1000

Input Description:
First line contains no. of test cases(Y). Next line contains a number N.
Next line contains n space separated numbers Next line contains a number T denoting the number of questions
asked from you regarding the given array. Next line contains T space separated numbers.

Output Description:
Print the occurrence of each number if present else “NOT PRESENT”

Sample Input :
10
1 1 1 2 2 2 3 8 9 7
5
1 2 3 0 5

Sample Output :
3 3 1 Not Present Not Present
"""
