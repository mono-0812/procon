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

n,q=IIS()
s=I()
acc=[0 for i in range(n+1)]
for i in range(1,n):
    if s[i-1]+s[i]=="AC":
        acc[i]=acc[i-1]+1
        continue
    acc[i]=acc[i-1]
for _ in range(q):
    l,r=IIS()
    print(acc[r-1]-acc[l-1])