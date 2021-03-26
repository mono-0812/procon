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
from fractions import gcd
A,B=IIS()
g=gcd(A,B)
def prime(n):
    i=2
    table=[]
    while i*i<=n:
        while n%i==0:
            n//=i
            table.append(i)
        i+=1
    if n>1:
        table.append(n)
    return table
print(len(set(prime(g)))+1)