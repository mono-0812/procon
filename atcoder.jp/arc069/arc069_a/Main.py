import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,m=IIS()
ans=0
if n*2<=m:
    ans+=n
    m-=n*2
    print(ans+m//4)
else:
    print(m//2)
