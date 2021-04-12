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
n,m,q=IIS()
ans=0
Q=[]
for i in range(q):a,b,c,d=IIS();Q.append((a,b,c,d))
for li in itertools.combinations_with_replacement(range(1,m+1),n):
    f=False
    p=0
    for i in range(n-1):
        if li[i]>li[i+1]:
            f=True
    if f:continue
    for a,b,c,d in Q:
        if li[b-1]-li[a-1]==c:
            p+=d
    ans=max(ans,p)
print(ans)