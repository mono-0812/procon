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

s=I()
def f(s,c):
    result=0
    while len(set(s))!=1:
        t=""
        for i in range(len(s)-1):
            if s[i]==c or s[i+1]==c:
                t+=c
            else:
                t+=s[i]
        s=t
        result+=1
    return result
result=INF
for c in set(s):
    result=min(result,f(s,c))
print(result)