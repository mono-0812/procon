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
def combinations_with_replacement_count(n, r):
    return comb(n + r - 1, r)
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
h,w=IIS()
if h==w==1:
    print("Draw")
    exit()
q=collections.deque()
A=[[0]*w for i in range(h)]
for i in range(h):
    a=I()
    for j in range(len(a)):
        A[i][j]=(1 if a[j]=="+" else -1)
dp=[[-INF for j in range(w)]for i in range(h)]
if (h+w)%2==1:
    dp[h-1][w-1]=A[h-1][w-1]
else:
    dp[h-1][w-1]=-(A[h-1][w-1])
i,j=0,0
for y in range(h-1,-1,-1):
    for x in range(w-1,-1,-1):
        if y==h-1 and x==w-1:
            dp[y][x]=0
        if y+1<h:
            dp[y][x]=max(dp[y][x],A[y+1][x]-dp[y+1][x])
        if x+1<w:
            dp[y][x]=max(dp[y][x],A[y][x+1]-dp[y][x+1])
ans = "Draw"
if 0 < dp[0][0]:
    ans = "Takahashi"
if dp[0][0] < 0:
    ans = "Aoki"
print(ans)
