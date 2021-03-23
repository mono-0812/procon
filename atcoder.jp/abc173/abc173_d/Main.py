import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()
ans=max(A)
A=sorted(A,reverse=True)[1:]
for i in range(n-2):
    ans+=A[i//2]
print(ans)