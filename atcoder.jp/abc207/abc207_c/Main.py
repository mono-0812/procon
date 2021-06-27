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
n=II()
ans=0
li=[]
for i in range(n):
    t,l,r=IIS()
    if t==1:
        li.append((l,r))
    if t==2:
        li.append((l,r-0.1))
    if t==3:
        li.append((l+0.1,r))
    if t==4:
        li.append((l+0.1,r-0.1))
for i in range(n):
    for j in range(i+1,n):
        l1,r1=li[i]
        l2,r2=li[j]
        if min(r1,r2)-max(l1,l2)>=0:
            ans+=1
print(ans)
