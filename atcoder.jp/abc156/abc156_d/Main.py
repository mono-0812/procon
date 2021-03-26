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
n,a,b=IIS()
def comb(a,b):
    c=1
    for i in range(b):
        c*=a-i
        c%=MOD
    d=1
    for i in range(b):
        d*=i+1
        d%=MOD
    return c*pow(d,MOD-2,MOD)
ans=pow(2,n,MOD)-1-comb(n,a)-comb(n,b)
print(ans%MOD)