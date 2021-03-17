import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
dp=[0 for _ in range(20)]
dp[0],dp[1],dp[2]=100,100,200
for i in range(3,20):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
print(dp[19])