import statistics
n=int(input(""))
N=list(map(int,input().strip().split()))[:n]
print(statistics.median(N))
