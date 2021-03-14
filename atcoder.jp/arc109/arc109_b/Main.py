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
L=0
R=n
lsr=0
if (n**2+n)//2<=n+1:
    print(1)
    exit()
while R>=L+2:
    mid=(R+L)//2
    if (mid**2+mid)//2<=n+1:
        L=mid
    else:
        R=mid
print(n+1-L)