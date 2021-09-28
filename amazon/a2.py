"""
Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
Input Size : N <= 100000
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
1 5
"""

#program
n= int(input())
l= list(map(int,input().strip().split()))[:n]

min_n=min(l)
max_x=max(l)

for idx, val in enumerate(l, start=1):
    if val==min_n:
        print(idx, end=" ")
        for idx1, val1 in enumerate(l, start=1):
            if val1==max_x:
                print(idx1, end=" ")
    


