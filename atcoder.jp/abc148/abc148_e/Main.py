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
val=10
ans=0
if n%2==1:
    print(0)
    exit()
while n>=val:
    ans+=n//val
    val*=5
print(ans)

