import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=998244353
##############################################################################
n=II()
A=LIIS()
A.sort()
ans=0
val=0
for i in range(n-2,-1,-1):
    val=(val*2+A[i+1])%MOD
    ans=(ans+val*A[i])%MOD
for i in range(n):
    ans=(ans+A[i]**2)%MOD
print(ans)



