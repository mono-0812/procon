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
h,w=IIS()
F=[I() for i in range(h)]
dp=[[INF]*w for i in range(h)]
val=0
dp[0][0]=1 if F[0][0]=="#" else 0
for i in range(h):
    for j in range(w):
        for k,l in [(1,0),(0,1)]:
            if 0<=k+i<h and 0<=j+l<w:
                if (F[k+i][j+l]==".") or (F[i][j]=="#" and F[i+k][j+l]=="#"):
                    dp[i+k][j+l]=min(dp[i][j],dp[i+k][j+l])
                else:
                    dp[i+k][j+l]=min(dp[i][j]+1,dp[i+k][j+l])
print(dp[h-1][w-1])