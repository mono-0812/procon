import bisect,collections,copy,heapq,itertools,math,string,sys,queue
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
##############################################################################
n,w=IIS()
W,V=[],[]
v=0
for i in range(n):
    ww,vv=IIS()
    W.append(ww)
    V.append(vv)
    v+=vv
dp=[[INF]*(v+1) for _ in range(n)]
for i in range(n):
    dp[i][0]=0
for i in range(n):
    for j in range(v+1):
        if dp[i-1][j-V[i]]+W[i]<=w:
        
            dp[i][j]=min(dp[i-1][j],dp[i-1][j-V[i]]+W[i])
        else:
            dp[i][j]=dp[i-1][j]
for i in range(v+1)[::-1]:
    for j in range(n):
        if dp[j][i]!=INF:
            print(i)
            exit()