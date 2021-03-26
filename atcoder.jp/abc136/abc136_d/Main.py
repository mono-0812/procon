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
s=list(I())
kids=[0]*len(s)
for d in ["R","L"]:
    c=0
    for i in range(len(s)):
        if s[i]==d:
            c+=1
        else:
            kids[i]+=c//2
            kids[i-1]+=(c+1)//2
            c=0
    s.reverse()
    kids.reverse()
print(*kids)