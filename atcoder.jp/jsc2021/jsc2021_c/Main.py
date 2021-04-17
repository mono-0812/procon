import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
A,B=IIS()
ans=1
for i in range(2,B+1):
    if (B//i)-((A-1)//i)>=2:
        ans=max(ans,i)
print(ans)
