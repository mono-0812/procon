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
n,ww=IIS()
dp=[[0]*(ww+1) for _ in range(n)]
w,v=[],[]
for i in range(n):
    W,V=IIS()
    w.append(W);v.append(V)
for i in range(n):
    for j in range(ww+1):
        if j-w[i]>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n-1][ww])