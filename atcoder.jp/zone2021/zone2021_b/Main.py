import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,d,h=IIS()
mxh=0
mxd=-1
ans=0
for i in range(n):
    dd,hh=IIS()
    yd=hh-h
    xd=dd-d
    ans=max(ans,h-d*(yd/xd))
print(max(0,ans))

