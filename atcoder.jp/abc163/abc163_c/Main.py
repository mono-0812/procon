import collections
n=int(input())
A=collections.Counter(list(map(int,input().split())))
for i in range(1,n+1):
    print(A[i])