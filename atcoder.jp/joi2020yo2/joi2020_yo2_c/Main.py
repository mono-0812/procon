import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
from typing import Deque
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
##############################################################################
n=II()
dp=[False for i in range(10**6*2)]
dp[n]=True
ans=0
for i in range(1,n)[::-1]:
    dp[i]=dp[sum(list(map(int,list(str(i)))))+i]
for i in range(n+1):
    ans+=dp[i]
print(ans)