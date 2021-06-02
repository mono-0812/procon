import collections
import itertools
import math
import decimal
import bisect
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n,k=IIS()
A=[LIIS() for i in range(n)]
l=0
r=0
for i in range(n):
    for j in range(n):
        r=max(r,A[i][j])
def solve(val):
    li=[[0]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            li[i][j]=li[i-1][j]+li[i][j-1]+(A[i-1][j-1]>val)-li[i-1][j-1]
    for i in range(1,n-k+2):
        for j in range(1,n-k+2):
            if li[i+k-1][j+k-1]-li[i-1][j+k-1]-li[i+k-1][j-1]+li[i-1][j-1]<=(k*k)//2:
                return True
    return False
while r-l>1:
    mid=(r+l)//2
    if solve(mid):
        r=mid
    else:
        l=mid
print(r)