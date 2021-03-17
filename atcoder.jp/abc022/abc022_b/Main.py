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
ans=0
path=[False for _ in range(10**5+1000)]
for i in range(n):
    val=II()
    if path[val-1]:
        ans+=1
    path[val-1]=True
print(ans)