import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
import decimal
##############################################################################
n=II()
A=LIIS()
A.sort()
ans=1
las=0
for i in range(n):
    ans=(ans*(A[i]-las+1))%MOD
    las=A[i]
print(ans)


