import bisect,collections,copy,heapq,itertools,math,string,sys,decimal,queue
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
n,k=IIS()
ans=decimal.Decimal(0)
for i in range(1,n+1):
    val=i
    cnt=decimal.Decimal(0)
    while val<k:
        cnt+=decimal.Decimal(1)
        val*=2
    ans+=decimal.Decimal(1)/(decimal.Decimal(2)**decimal.Decimal(cnt))
print(ans/n)