import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
from typing import Union, ValuesView
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
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out
ragen=range
INF=10**20
MOD=10**9+7
from decimal import Decimal as d, DefaultContext
##############################################################################
n,m=IIS()
ans=[["",n] for i in range(n)]
s=[I() for i in range(m)]
s.sort(key=lambda x:len(x))
h=0
f=False
for i in range(m):
    v=s[i]
    while ans[h][1]<len(v):
        h+=1
        if n<=h:
            f=True
            break
    if f:break
    ans[h][0]+=v
    ans[h][1]-=len(v)
for i in range(n):
    print(ans[i][0]+"."*(ans[i][1]))