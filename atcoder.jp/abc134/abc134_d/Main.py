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
B=[0]*n
for i in reversed(range(1,n+1)):
    val=0
    for j in range(i-1,n,i):
        val+=B[j]
    if val%2!=A[i-1]:
        B[i-1]=1
print(sum(B))
for i in range(len(B)):
    if B[i]:
        print(i+1)