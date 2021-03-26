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
n=II()
A=[[] for i in range(n)]
for i in range(n):
    m=II()
    for j in range(m):
        x,y=IIS()
        A[i].append((x-1,y))
ans=0
for i in range(1<<n):
    ok=True
    cnt=0
    for j in range(n):
        if (i>>j&1):
            cnt+=1
    for j in range(n):
        if (i>>j&1)==1:
            for x,y in A[j]:
                if y==0:
                    if (i>>x&1)==1:
                        ok=False
                elif y==1:
                    if (i>>x&1)==0:
                        ok=False
    if ok:
        ans=max(ans,cnt)
print(ans)