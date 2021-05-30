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
n=II()
A=[II() for i in range(n)]
A.sort(reverse=True)
if n%2==0:
    ans=0
    for i in range(n//2-1):
        ans+=A[i]*2
    ans+=A[n//2-1]
    ans-=A[n//2]
    for i in range(n//2+1,n):
        ans-=A[i]*2
    print(ans)
else:
    ans=0
    for i in range(n//2-1):
        ans+=A[i]*2
    ans+=A[n//2-1]
    ans+=A[n//2]
    for i in range(n//2+1,n):
        ans-=A[i]*2
    ans2=0
    for i in range(n//2):
        ans2+=A[i]*2
    ans2-=A[n//2]
    ans2-=A[n//2+1]
    for i in range(n//2+2,n):
        ans2-=A[i]*2
    print(max(ans2,ans))
