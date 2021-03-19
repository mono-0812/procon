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
dp=[[0 for _ in range(n+1)] for _ in range(3)]
for i in range(1,n+1):
    a,b,c=IIS()
    #0 a　1 b 3 c
    dp[1][i]=max(dp[0][i-1]+b,dp[2][i-1]+b)
    dp[2][i]=max(dp[1][i-1]+c,dp[0][i-1]+c)
    dp[0][i]=max(dp[2][i-1]+a,dp[1][i-1]+a)
print(max(dp[1][n],max(dp[2][n],dp[0][n])))