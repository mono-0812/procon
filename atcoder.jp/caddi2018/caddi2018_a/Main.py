import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
from typing import Counter
input = lambda: sys.stdin.readline().rstrip()
start_time=time.time()
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
def nt(): print(time.time()-start_time);return
def comb(n, r):return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def tr():pass
def try_run():
    try:tr()
    except:pass
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
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
ragen=range
INF=10**18
MOD=998244353
##############################################################################
n,p=IIS()
li=collections.Counter(prime_factorize(p))
ans=1
for i in li.keys():
    if n<=li[i]:
        ans*=i**(li[i]//n)
print(ans)