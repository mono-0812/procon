import bisect,collections,copy,heapq,itertools,math,string,sys,queue
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
n,m,k=IIS()
A=LIIS();B=LIIS()
AS=list(itertools.accumulate(A));BS=list(itertools.accumulate(B))
ans=0
for i in range(n):
    if k-AS[i]<0:
        continue
    ans=max(ans,bisect.bisect_right(BS,k-AS[i])+i+1)
ans=max(ans,bisect.bisect_right(BS,k))
print(ans)

