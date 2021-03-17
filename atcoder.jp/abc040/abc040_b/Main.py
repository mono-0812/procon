import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
ans=INF
for v in range(1,n+1):
    s=n//v
    ans=min(ans,abs(s-v)+(n-(s*v)))
print(ans)