import collections
import itertools
import math
import decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
A=LIIS()
A.sort()
v=0
ans=0
for i in range(n):
    v+=A[i]
    if v*2>=A[min(i+1,n-1)]:
        ans+=1
    else:
        ans=0
print(ans)