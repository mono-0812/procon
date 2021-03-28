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
A=LIIS()
ans=INF
def solve(num,li):
    global ans
    if num==n:
        val=li[0]
        if len(li)>=2:
            for i in li[1:]:
                val^=i
        return val
    li.append(A[num])
    ans=min(solve(num+1,li),ans)
    li.pop()
    li[-1]|=A[num]
    ans=min(solve(num+1,li),ans)
    return 10**9+7
solve(1,[A[0]])
if ans==INF:
    print(A[0])
    exit()
print(ans)