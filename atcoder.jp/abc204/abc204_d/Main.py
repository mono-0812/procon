import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
start_time=time.time()
def nt(): print(time.time()-start_time);return
def chmax(a: list, b: list) -> bool:
     assert len(a) == len(b) == 1, "1要素のlistを指定してください"
     if a[0] < b[0]:
         a[0] = b[0]
         return True
     return False
def chmin(a: list, b: list) -> bool:
    assert len(a) == len(b) == 1, "1要素のlistを指定してください"
    if a[0] > b[0]:
        a[0] = b[0]
        return True
    return False
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ragen=range
INF=10**10
MOD=10**9+7
from decimal import Decimal as d
##############################################################################
n=II()
dp=[[False]*(10**5+10) for i in range(n+5)]
T=LIIS()
sm=sum(T)
ans=sum(T)
dp[0][0]=True
for i in range(n):
    for j in range(10**5+10):
        dp[i+1][j]|=dp[i][j]
        if j>=T[i]:
            dp[i+1][j]|=dp[i][j-T[i]]
            if dp[i+1][j]:
                ans=min(ans,max(sm-j,j))
print(ans)
