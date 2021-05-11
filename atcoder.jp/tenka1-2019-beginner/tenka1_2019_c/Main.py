import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
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
ragen=range
INF=10**18
MOD=998244353
##############################################################################
n=II()
s=I()
bc=[0]
wc=[0]
for i in range(n):
    if s[i]=="#":
        bc.append(bc[i]+1)
    else:
        bc.append(bc[i])
for i in range(n)[::-1]:
    if s[i]==".":
        wc.append(wc[n-i-1]+1)
    else:
        wc.append(wc[n-i-1])
bc.pop()
wc.reverse()
ans=INF
wc.pop(0)
for i in range(n):
    ans=min(ans,bc[i]+wc[i])
print(ans)