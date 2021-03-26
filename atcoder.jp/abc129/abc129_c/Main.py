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
n,m=IIS()
dp=[0]*(n+1)
dp[0]=1
s=set()
for i in range(m):
    a = int(input())
    s.add(a)
for i in range(n):
    if i in s:
        continue
    for j in range(1,3):
        if i+j<=n:
            dp[i+j]=(dp[i]+dp[i+j])%MOD
print(dp[-1])