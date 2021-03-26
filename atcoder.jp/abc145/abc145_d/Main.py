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
x,y=IIS()
n=(-1*x+2*y)//3
m=(2*x-y)//3
if n<0 or m<0 or (x+y)%3:
    print(0);exit()
def comb(N,R):
    U=1;D=1
    for i in range(R):
        U*=N-i
        U%=MOD
        D*=i+1
        D%=MOD
    return U*pow(D,MOD-2,MOD)%MOD
print(comb(n+m,n))

