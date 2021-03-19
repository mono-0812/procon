import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
s=II()
dp=[0 for _ in range(s+1)]
dp[0]=1
x=0
for i in range(3,s+1):
    x+=dp[i-3]
    dp[i]=x%MOD
print(dp[s]%MOD)